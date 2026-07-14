import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.convert_papers import (
    already_converted,
    discard_invalid_page_outputs,
    invalid_page_files,
)
from scripts.extraction_planning import (
    format_page_spec,
    plan_chapter_inputs,
    validate_chapter_units,
)
from scripts.extract_papers import (
    MAX_CHARS,
    call_model,
    chapter_cache_signature,
    dry_run_plan,
    public_source_metadata,
    summary_header,
)
from scripts.paper_sources import RESTRICTED_NOTICE, paper_md_path


ROOT = Path(__file__).resolve().parent.parent


class RestrictedSourceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = json.loads((ROOT / "papers/papers.json").read_text())["papers"]
        cls.by_key = {paper["key"]: paper for paper in cls.papers}

    def test_restricted_catalog_entries_have_public_provenance_only(self):
        expected = {
            "t1-ssth",
            "t2-gtvh",
            "t4-linguistic-analysis-of-jokes",
            "t5-incongruity-resolution",
        }
        restricted = {
            paper["key"] for paper in self.papers if paper["status"] == "restricted"
        }

        self.assertEqual(expected, restricted)
        self.assertEqual("unavailable", self.by_key["t3-inside-jokes"]["status"])
        for key in restricted:
            paper = self.by_key[key]
            self.assertEqual(RESTRICTED_NOTICE, paper["access_notice"])
            self.assertTrue(paper["official_sources"])
            self.assertNotIn("pdf_path", paper)
            self.assertNotIn("md_path", paper)
            self.assertNotIn("md_pages_dir", paper)
            self.assertTrue(paper["restricted_source"]["sha256"])
        self.assertIn("papers/private/", (ROOT / ".gitignore").read_text())

    def test_t5_marks_oring_as_pending(self):
        sources = self.by_key["t5-incongruity-resolution"]["official_sources"]
        self.assertEqual([True, False], [source["consulted"] for source in sources])
        self.assertIn(
            "Oring (2003) remains pending",
            self.by_key["t5-incongruity-resolution"]["restricted_source"]["scope"],
        )

    def test_partial_single_pass_prompt_excludes_unconsulted_work(self):
        paper = self.by_key["t5-incongruity-resolution"]
        with patch("scripts.extract_papers.call_json_response", return_value={}) as call:
            call_model(None, paper, "Suls chapter text", [])
        prompt = call.call_args.kwargs["user_content"]
        self.assertIn("Suls (1972) chapter only", prompt)
        self.assertIn("UNCONSULTED CATALOG SOURCES", prompt)
        self.assertIn("Oring book at University of Illinois Press", prompt)

    def test_downloaded_public_source_has_a_conversion_target_before_md_metadata(self):
        target = paper_md_path(
            ROOT,
            {"key": "new-paper", "status": "downloaded"},
        )
        self.assertEqual(
            ROOT / "papers/md/new-paper/new-paper.md",
            target,
        )

    def test_restricted_summary_emits_publishers_but_no_full_text_links(self):
        paper = self.by_key["t5-incongruity-resolution"]
        extract = {
            "title": paper["title"],
            "authors": ["Jerry Suls"],
        }
        header = summary_header(paper, extract, {})

        self.assertIn(RESTRICTED_NOTICE, header)
        for source in paper["official_sources"]:
            self.assertIn(source["url"], header)
        self.assertNotIn("../pdfs/", header)
        self.assertNotIn("../md/", header)
        self.assertNotIn("local PDF", header)
        self.assertNotIn("full markdown", header)

        metadata = public_source_metadata(paper, "abc123", {"strategy": "single-pass"})
        self.assertEqual("restricted", metadata["source_access"])
        self.assertFalse(metadata["catalog_entry_source_coverage_complete"])
        self.assertNotIn("source_md", metadata)
        self.assertNotIn("pdf_path", json.dumps(metadata))

    def test_generated_manifest_has_no_restricted_full_text_links(self):
        manifest = (ROOT / "papers/MANIFEST.md").read_text()
        for key in (
            "t1-ssth",
            "t2-gtvh",
            "t4-linguistic-analysis-of-jokes",
            "t5-incongruity-resolution",
        ):
            self.assertNotIn(f"pdfs/{key}", manifest)
            self.assertNotIn(f"md/{key}", manifest)
        for key in (
            "t1-ssth",
            "t2-gtvh",
            "t4-linguistic-analysis-of-jokes",
            "t5-incongruity-resolution",
        ):
            for source in self.by_key[key]["official_sources"]:
                self.assertIn(source["url"], manifest)
        self.assertIn(RESTRICTED_NOTICE, manifest)

    def test_book_page_plans_cover_every_physical_page_exactly_once(self):
        for key in ("t1-ssth", "t4-linguistic-analysis-of-jokes"):
            paper = self.by_key[key]
            units = validate_chapter_units(paper)
            pages = [page for unit in units for page in unit["pages"]]
            page_count = paper["restricted_source"]["page_count"]
            self.assertEqual(list(range(1, page_count + 1)), pages, key)

    def test_chapter_inputs_split_only_on_page_boundaries(self):
        paper = {
            "key": "test-book",
            "status": "restricted",
            "restricted_source": {"page_count": 4},
            "extraction": {
                "strategy": "chapters",
                "units": [
                    {"id": "chapter-1", "title": "Chapter 1", "pages": "1-4"}
                ],
            },
        }
        with tempfile.TemporaryDirectory() as temporary:
            pages_dir = Path(temporary)
            for page in range(1, 5):
                (pages_dir / f"page_{page:04d}.md").write_text("x" * 80)
            planned = plan_chapter_inputs(paper, pages_dir, max_chars=130)

        self.assertEqual(4, len(planned))
        self.assertEqual(
            [1, 2, 3, 4], [page for unit in planned for page in unit["pages"]]
        )
        self.assertTrue(all(unit["char_count"] <= 130 for unit in planned))
        self.assertEqual("1,3-4,6", format_page_spec([1, 3, 4, 6]))

    def test_chapter_cache_signature_covers_the_full_request_contract(self):
        paper = {
            "key": "test-book",
            "ref": "T0",
            "title": "Test Book",
            "extraction": {"strategy": "chapters"},
        }
        unit = {
            "id": "chapter-1",
            "title": "Chapter 1",
            "page_spec": "1-2",
            "char_count": 12,
            "markdown": "chapter text",
        }
        signature = chapter_cache_signature(
            paper,
            "source-hash",
            unit,
            ["Dataset One"],
        )

        with patch(
            "scripts.extract_papers.CHAPTER_SYSTEM_PROMPT",
            "revised chapter prompt",
        ):
            prompt_changed = chapter_cache_signature(
                paper,
                "source-hash",
                unit,
                ["Dataset One"],
            )
        with patch(
            "scripts.extract_papers.CHAPTER_SCHEMA",
            {"type": "object", "properties": {"revised": {"type": "string"}}},
        ):
            schema_changed = chapter_cache_signature(
                paper,
                "source-hash",
                unit,
                ["Dataset One"],
            )
        datasets_changed = chapter_cache_signature(
            paper,
            "source-hash",
            unit,
            ["Dataset Two"],
        )

        self.assertNotEqual(
            signature["chapter_request_sha256"],
            prompt_changed["chapter_request_sha256"],
        )
        self.assertNotEqual(
            signature["chapter_request_sha256"],
            schema_changed["chapter_request_sha256"],
        )
        self.assertNotEqual(
            signature["chapter_request_sha256"],
            datasets_changed["chapter_request_sha256"],
        )

    def test_oversized_single_pass_is_blocked_not_truncated(self):
        paper = {
            "key": "test-article",
            "status": "restricted",
            "restricted_source": {"page_count": 1},
            "extraction": {"strategy": "single"},
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            md_path = root / "papers/private/test-article/md/test-article.md"
            md_path.parent.mkdir(parents=True)
            md_path.write_text("x" * (MAX_CHARS + 1))
            with patch("scripts.extract_papers.ROOT", root):
                plan = dry_run_plan(paper)

        self.assertEqual("blocked", plan["status"])
        self.assertEqual(MAX_CHARS + 1, plan["source_characters"])

    def test_serialized_response_page_is_removed_before_resume(self):
        paper = {
            "key": "test-book",
            "status": "restricted",
            "restricted_source": {"page_count": 2},
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            out_dir = root / "papers/private/test-book/md"
            pages_dir = out_dir / "pages"
            pages_dir.mkdir(parents=True)
            (pages_dir / "page_0001.md").write_text("Valid page\n")
            (pages_dir / "page_0002.md").write_text("Response(id='raw')\n")
            (out_dir / "test-book.md").write_text("stale combined\n")
            (out_dir / "manifest.jsonl").write_text(
                '{"page": 1}\n{"page": 2}\n', encoding="utf-8"
            )

            with patch("scripts.convert_papers.ROOT", root):
                self.assertEqual(1, len(invalid_page_files(paper)))
                self.assertFalse(already_converted(paper))
                self.assertEqual([2], discard_invalid_page_outputs(paper))

            self.assertTrue((pages_dir / "page_0001.md").exists())
            self.assertFalse((pages_dir / "page_0002.md").exists())
            self.assertFalse((out_dir / "test-book.md").exists())
            self.assertEqual(
                '{"page": 1}\n',
                (out_dir / "manifest.jsonl").read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()

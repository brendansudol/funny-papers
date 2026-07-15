import hashlib
import re
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZIP_STORED, ZipFile

from scripts.build_ebook import (
    EDITION_CONFIG,
    EbookBuildError,
    REPOSITORY_URL,
    assemble_manuscript,
    load_catalog,
    normalize_epub_archive,
    rewrite_relative_links,
    sections_in_order,
    summary_papers,
    validate_public_manuscript,
)
from scripts.paper_sources import RESTRICTED_NOTICE


ROOT = Path(__file__).resolve().parent.parent


class EbookBuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()
        cls.papers = summary_papers(cls.catalog)
        cls.guide = assemble_manuscript("guide", catalog=cls.catalog)
        cls.complete = assemble_manuscript("complete", catalog=cls.catalog)

    def test_summary_selection_is_complete_and_canonically_ordered(self):
        expected = [
            paper["key"]
            for paper in self.catalog["papers"]
            if paper["status"] in {"converted", "restricted"}
        ]

        self.assertEqual(115, len(self.papers))
        self.assertEqual(expected, [paper["key"] for paper in self.papers])
        self.assertNotIn("t3-inside-jokes", expected)

    def test_guide_edition_promotes_sections_and_rewrites_repo_links(self):
        self.assertIn('title: "Getting the Joke: Field Guide"', self.guide)
        self.assertIn('subtitle: "Humor and Large Language Models"', self.guide)
        self.assertIn('author: "funny-papers project"', self.guide)
        self.assertIn("\n# A Framework for Reading the Field\n", self.guide)
        self.assertNotIn("\n## A Framework for Reading the Field\n", self.guide)
        self.assertNotIn("{#summary-", self.guide)
        self.assertIn(
            f"{REPOSITORY_URL}/blob/main/papers/EVIDENCE.md",
            self.guide,
        )
        validate_public_manuscript(self.guide)

    def test_complete_edition_has_every_summary_once_in_catalog_order(self):
        grouped_papers = [
            paper
            for _, section_papers in sections_in_order(self.papers)
            for paper in section_papers
        ]
        anchors = [f"{{#summary-{paper['key']}}}" for paper in grouped_papers]

        self.assertIn('title: "Getting the Joke: Complete Edition"', self.complete)
        self.assertEqual(115, self.complete.count("{#summary-"))
        positions = [self.complete.index(anchor) for anchor in anchors]
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(len(positions), len(set(positions)))
        self.assertNotIn("{#summary-t3-inside-jokes}", self.complete)
        self.assertIn("T3 (Inside Jokes: Using Humor to Reverse-Engineer the Mind)", self.complete)

    def test_complete_edition_preserves_section_order_and_readable_hierarchy(self):
        section_names = [section for section, _ in sections_in_order(self.papers)]
        section_positions = [self.complete.index(f"\n## {section}\n") for section in section_names]

        self.assertEqual(section_positions, sorted(section_positions))
        self.assertIn("\n# Part I — Field Guide {epub:type=part}\n", self.complete)
        self.assertIn("\n# Part II — Paper Summaries {epub:type=part}\n", self.complete)
        self.assertIn("\n#### In brief\n", self.complete)
        self.assertNotIn("\n## TL;DR\n", self.complete)

    def test_summary_navigation_links_are_replaced_with_primary_sources(self):
        first = next(paper for paper in self.papers if paper["key"] == "01-androids-electric-sheep")

        self.assertIn(first["page_url"], self.complete)
        self.assertNotIn("../pdfs/01-androids-electric-sheep.pdf", self.complete)
        self.assertNotIn("../md/01-androids-electric-sheep", self.complete)
        self.assertNotIn("../extracts/01-androids-electric-sheep.json", self.complete)
        validate_public_manuscript(self.complete)

    def test_prompt_placeholders_are_escaped_for_valid_epub_xhtml(self):
        self.assertIn("&lt;image&gt;", self.complete)
        self.assertIn("&lt;topic&gt;", self.complete)
        self.assertNotIn("<image>", self.complete)
        self.assertNotIn("<topic>", self.complete)

    def test_restricted_summaries_keep_notices_and_official_source_status(self):
        restricted = [paper for paper in self.papers if paper["status"] == "restricted"]
        summaries_part = self.complete.split(
            "# Part II — Paper Summaries {epub:type=part}", 1
        )[1]

        self.assertEqual(4, len(restricted))
        self.assertEqual(4, summaries_part.count(RESTRICTED_NOTICE))
        for paper in restricted:
            for source in paper["official_sources"]:
                self.assertIn(source["url"], self.complete)
                status = "consulted" if source["consulted"] else "not yet consulted"
                self.assertIn(status, self.complete)

    def test_manuscripts_are_stable_for_unchanged_sources(self):
        self.assertEqual(
            self.guide,
            assemble_manuscript("guide", catalog=self.catalog),
        )
        self.assertEqual(
            self.complete,
            assemble_manuscript("complete", catalog=self.catalog),
        )

    def test_committed_epubs_match_current_manuscripts(self):
        manuscripts = {"guide": self.guide, "complete": self.complete}

        for edition, manuscript in manuscripts.items():
            with self.subTest(edition=edition):
                identifier_match = re.search(
                    r'^identifier: "([^"]+)"$', manuscript, re.MULTILINE
                )
                self.assertIsNotNone(identifier_match)
                expected_identifier = identifier_match.group(1)
                epub_path = ROOT / "dist" / EDITION_CONFIG[edition]["filename"]
                self.assertTrue(epub_path.is_file(), f"Missing {epub_path}")

                with ZipFile(epub_path) as archive:
                    opf_names = [
                        name for name in archive.namelist() if name.endswith(".opf")
                    ]
                    self.assertEqual(1, len(opf_names))
                    self.assertIn(
                        expected_identifier.encode("utf-8"),
                        archive.read(opf_names[0]),
                    )

    def test_relative_link_rewriter_preserves_fragments(self):
        rewritten = rewrite_relative_links(
            "See [evidence](papers/EVIDENCE.md#scope).",
            ROOT / "humor-and-llms-field-guide.md",
        )

        self.assertEqual(
            f"See [evidence]({REPOSITORY_URL}/blob/main/papers/EVIDENCE.md#scope).",
            rewritten,
        )

    def test_public_validation_rejects_local_or_relative_links(self):
        for manuscript in (
            "[paper](../pdfs/example.pdf)",
            "[notes](papers/notes.md)",
            "[private](https://example.test/papers/private/book.md)",
            "file:///Users/example/book.md",
        ):
            with self.subTest(manuscript=manuscript):
                with self.assertRaises(EbookBuildError):
                    validate_public_manuscript(manuscript)

    def test_epub_archive_normalization_is_reproducible(self):
        with tempfile.TemporaryDirectory() as temporary:
            epub_path = Path(temporary) / "book.epub"
            with ZipFile(epub_path, "w") as archive:
                archive.writestr("mimetype", "application/epub+zip", ZIP_STORED)
                archive.writestr(
                    "EPUB/content.opf",
                    '<meta property="dcterms:modified">2026-07-14T12:34:56Z</meta>',
                    ZIP_DEFLATED,
                )
                archive.writestr("EPUB/chapter.xhtml", "<p>hello</p>", ZIP_DEFLATED)

            normalize_epub_archive(epub_path, "2026-07-13")
            first_hash = hashlib.sha256(epub_path.read_bytes()).hexdigest()
            normalize_epub_archive(epub_path, "2026-07-13")
            second_hash = hashlib.sha256(epub_path.read_bytes()).hexdigest()

            self.assertEqual(first_hash, second_hash)
            with ZipFile(epub_path) as archive:
                infos = archive.infolist()
                self.assertEqual("mimetype", infos[0].filename)
                self.assertEqual(ZIP_STORED, infos[0].compress_type)
                self.assertEqual((2026, 7, 13, 0, 0, 0), infos[0].date_time)
                self.assertIn(
                    b"2026-07-13T00:00:00Z",
                    archive.read("EPUB/content.opf"),
                )


if __name__ == "__main__":
    unittest.main()

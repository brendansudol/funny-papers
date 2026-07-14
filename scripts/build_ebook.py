#!/usr/bin/env python3
"""Build reflowable EPUB reader editions of the guide and paper summaries.

The canonical Markdown remains unchanged.  This script assembles a temporary,
reader-facing manuscript, removes repository-local research links, renders it
with Pandoc, and optionally validates the result with EPUBCheck.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path, PurePosixPath
from urllib.parse import quote, urlsplit, urlunsplit
from zipfile import ZIP_DEFLATED, ZIP_STORED, ZipFile, ZipInfo

try:
    from paper_sources import access_notice, is_restricted, public_source_links
except ModuleNotFoundError:  # Imported as scripts.build_ebook in tests/tools.
    from scripts.paper_sources import (
        access_notice,
        is_restricted,
        public_source_links,
    )


ROOT = Path(__file__).resolve().parent.parent
GUIDE_PATH = ROOT / "humor-and-llms-field-guide.md"
CATALOG_PATH = ROOT / "papers" / "papers.json"
SUMMARIES_DIR = ROOT / "papers" / "summaries"
CSS_PATH = ROOT / "assets" / "ebook.css"
DEFAULT_OUTPUT_DIR = ROOT / "dist"
REPOSITORY_URL = "https://github.com/brendansudol/funny-papers"
READY_STATUSES = {"converted", "restricted"}

EDITION_CONFIG = {
    "guide": {
        "subtitle": "Humor and Large Language Models: A Field Guide",
        "description": (
            "A curated guide to humor theory, computational humor, and the "
            "large-language-model era."
        ),
        "filename": "humor-and-llms-field-guide.epub",
        "toc_depth": 2,
        "split_level": 1,
    },
    "complete": {
        "subtitle": "Humor and Large Language Models: Field Guide and Paper Companion",
        "description": (
            "A curated field guide to humor and large language models, followed "
            "by catalog-ordered summaries of the available primary sources."
        ),
        "filename": "humor-and-llms-complete.epub",
        "toc_depth": 3,
        "split_level": 3,
    },
}

SUMMARY_HEADING_RENAMES = {
    "TL;DR": "In brief",
    "Problem & Motivation": "Problem and motivation",
    "Data & Experimental Setup": "Data and study design",
    "Limitations & Caveats": "Limitations and caveats",
}

LINK_TARGET_RE = re.compile(r"\]\((?P<target><[^>]+>|[^)\s]+)")
RELATIVE_LINK_RE = re.compile(
    r"(?P<prefix>!?\[[^\]]*\]\()"
    r"(?P<target><[^>]+>|[^)\s]+)"
    r"(?P<suffix>[^)]*\))"
)
HEADING_RE = re.compile(r"^(?P<marks>#{1,6}) (?P<title>.*)$")
PSEUDO_TAG_RE = re.compile(r"<(?P<tag>[A-Za-z][A-Za-z0-9_-]*)>")
DCTERMS_MODIFIED_RE = re.compile(
    rb'(?P<prefix><meta property="dcterms:modified">)[^<]+'
    rb'(?P<suffix></meta>)'
)

FORBIDDEN_PUBLIC_MARKERS = (
    "papers/private/",
    "papers/pdfs/",
    "papers/md/",
    "papers/extracts/",
    "papers/runs/",
    "../pdfs/",
    "../md/",
    "../extracts/",
    "manifest.jsonl",
    ".progress.jsonl",
    "file://",
    "/users/",
    "local pdf",
    "full markdown",
)


class EbookBuildError(RuntimeError):
    """Raised when source or tool validation prevents a trustworthy build."""


def load_catalog(catalog_path: Path = CATALOG_PATH) -> dict:
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    papers = catalog.get("papers")
    if not isinstance(papers, list):
        raise EbookBuildError(f"Catalog has no paper list: {catalog_path}")
    keys = [paper.get("key") for paper in papers]
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    if duplicates:
        raise EbookBuildError(f"Duplicate catalog keys: {', '.join(duplicates)}")
    return catalog


def summary_papers(
    catalog: dict,
    summaries_dir: Path = SUMMARIES_DIR,
) -> list[dict]:
    """Return analysis-ready papers in canonical order, failing on drift."""
    papers = catalog["papers"]
    catalog_keys = {paper["key"] for paper in papers}
    summary_keys = {path.stem for path in summaries_dir.glob("*.md")}
    unknown = sorted(summary_keys - catalog_keys)
    if unknown:
        raise EbookBuildError(
            "Summary files are missing catalog entries: " + ", ".join(unknown)
        )

    expected = [paper for paper in papers if paper.get("status") in READY_STATUSES]
    missing = [paper["key"] for paper in expected if paper["key"] not in summary_keys]
    if missing:
        raise EbookBuildError(
            "Catalog-ready papers are missing summaries: " + ", ".join(missing)
        )
    return expected


def yaml_string(value: object) -> str:
    """JSON strings are also valid YAML strings and need no extra dependency."""
    return json.dumps(str(value), ensure_ascii=False)


def markdown_metadata(edition: str, catalog: dict, body: str) -> str:
    config = EDITION_CONFIG[edition]
    source_digest = hashlib.sha256(
        (edition + "\0" + body).encode("utf-8")
    ).hexdigest()
    values = {
        "title": "Getting the Joke",
        "subtitle": config["subtitle"],
        "author": "funny-papers project",
        "lang": "en-US",
        "date": catalog.get("updated") or catalog.get("created") or "",
        "identifier": f"urn:sha256:{source_digest}",
        "description": config["description"],
    }
    lines = ["---"]
    lines.extend(f"{key}: {yaml_string(value)}" for key, value in values.items())
    lines.extend(["---", ""])
    return "\n".join(lines)


def strip_guide_title(markdown: str) -> str:
    lines = markdown.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise EbookBuildError("The field guide must begin with one level-1 title")
    lines = lines[1:]
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and re.fullmatch(r"\*[^*].*\*", lines[0].strip()):
        lines.pop(0)
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(lines).rstrip() + "\n"


def promote_guide_headings(markdown: str) -> str:
    lines: list[str] = []
    for line in markdown.splitlines():
        match = HEADING_RE.match(line)
        if match and len(match.group("marks")) >= 2:
            line = "#" * (len(match.group("marks")) - 1) + " " + match.group("title")
        lines.append(line)
    return "\n".join(lines).rstrip() + "\n"


def _is_external_or_internal_target(target: str) -> bool:
    lowered = target.lower()
    return (
        target.startswith("#")
        or lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("mailto:")
        or lowered.startswith("data:")
    )


def _repository_url_for_relative_target(target: str, source_path: Path) -> str:
    unwrapped = target[1:-1] if target.startswith("<") and target.endswith(">") else target
    parsed = urlsplit(unwrapped)
    if parsed.scheme or parsed.netloc:
        return target

    source_relative = source_path.resolve().relative_to(ROOT.resolve())
    normalized = PurePosixPath(source_relative.parent, parsed.path)
    parts: list[str] = []
    for part in normalized.parts:
        if part in ("", "."):
            continue
        if part == "..":
            if not parts:
                raise EbookBuildError(f"Link escapes repository: {target}")
            parts.pop()
        else:
            parts.append(part)
    repo_path = "/".join(parts)
    if not repo_path:
        return REPOSITORY_URL
    url = f"{REPOSITORY_URL}/blob/main/{quote(repo_path, safe='/')}"
    return urlunsplit(("https", "github.com", urlsplit(url).path, parsed.query, parsed.fragment))


def rewrite_relative_links(markdown: str, source_path: Path) -> str:
    """Turn repository-relative reading links into useful public web links."""

    def replace(match: re.Match[str]) -> str:
        target = match.group("target")
        unwrapped = (
            target[1:-1]
            if target.startswith("<") and target.endswith(">")
            else target
        )
        if _is_external_or_internal_target(unwrapped):
            return match.group(0)
        public_target = _repository_url_for_relative_target(target, source_path)
        return match.group("prefix") + public_target + match.group("suffix")

    return RELATIVE_LINK_RE.sub(replace, markdown)


def escape_link_label(label: object) -> str:
    return str(label).replace("[", "\\[").replace("]", "\\]")


def source_note(paper: dict) -> list[str]:
    links: list[str] = []
    for source in public_source_links(paper):
        label = source.get("label") or "Paper page"
        if label == "publisher page" and not is_restricted(paper):
            label = "Paper page"
        if source.get("consulted") is True:
            label = f"{label} (consulted)"
        elif source.get("consulted") is False:
            label = f"{label} (not yet consulted)"
        links.append(f"[{escape_link_label(label)}](<{source['url']}>)")
    if not links:
        raise EbookBuildError(f"{paper['key']} has no public primary-source URL")

    lines = ["::: {.source-note}", "**Primary source:** " + " · ".join(links), ":::"]
    if is_restricted(paper):
        lines.extend(
            [
                "",
                "::: {.restricted-notice}",
                access_notice(paper),
                ":::",
            ]
        )
    return lines


def render_summary(paper: dict, summary_path: Path) -> str:
    lines = summary_path.read_text(encoding="utf-8").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise EbookBuildError(f"Summary must begin with a title: {summary_path}")
    title = lines[0][2:].strip()
    body_start = next(
        (index for index, line in enumerate(lines[1:], start=1) if line.startswith("## ")),
        None,
    )
    if body_start is None:
        raise EbookBuildError(f"Summary has no section headings: {summary_path}")
    byline = next(
        (line.strip() for line in lines[1:body_start] if line.strip().startswith("**")),
        None,
    )
    if byline is None:
        raise EbookBuildError(f"Summary has no author/venue byline: {summary_path}")

    rendered = [
        f"### {title} {{#summary-{paper['key']}}}",
        "",
        "::: {.paper-meta}",
        byline,
        ":::",
        "",
    ]
    rendered.extend(source_note(paper))
    rendered.append("")

    for line in lines[body_start:]:
        # Prompt templates such as ``<image>`` are prose placeholders, not HTML.
        # Escaping them here prevents Pandoc from emitting invalid XHTML while
        # leaving the canonical generated summary untouched.
        line = PSEUDO_TAG_RE.sub(
            lambda match: f"&lt;{match.group('tag')}&gt;",
            line,
        )
        match = HEADING_RE.match(line)
        if match:
            level = len(match.group("marks"))
            heading = SUMMARY_HEADING_RENAMES.get(
                match.group("title"), match.group("title")
            )
            line = "#" * min(level + 2, 6) + " " + heading
        rendered.append(line)
    return "\n".join(rendered).rstrip() + "\n"


def sections_in_order(papers: list[dict]) -> list[tuple[str, list[dict]]]:
    sections: dict[str, list[dict]] = {}
    for paper in papers:
        sections.setdefault(paper["section"], []).append(paper)
    return list(sections.items())


def about_this_edition(edition: str, catalog: dict, summary_count: int) -> str:
    source_date = catalog.get("updated") or catalog.get("created") or "unknown"
    scope = (
        "the field guide"
        if edition == "guide"
        else f"the field guide and {summary_count} public paper summaries"
    )
    return f"""# About this edition {{epub:type=backmatter}}

This reader edition contains {scope}, assembled from the
[`funny-papers` research library](<{REPOSITORY_URL}>). Its source catalog was
last updated {source_date}.

The guide is curated analysis. Paper summaries and full-text transcriptions are
research and navigation aids, not authoritative editions of the cited works.
Verify claims and quotations against the primary source before relying on them.
Copyright in the cited works remains with their authors and publishers.

Restricted primary sources are represented only by derived summaries and
official publisher links. Their PDFs, transcriptions, page files, intermediate
extracts, manifests, and run logs are not included in this ebook.

For audit scope and evidence qualifications, see the repository's
[`EVIDENCE.md`](<{REPOSITORY_URL}/blob/main/papers/EVIDENCE.md>) and
[`DISCREPANCIES.md`](<{REPOSITORY_URL}/blob/main/papers/DISCREPANCIES.md>).
"""


def assemble_manuscript(
    edition: str,
    *,
    root: Path = ROOT,
    catalog: dict | None = None,
) -> str:
    if edition not in EDITION_CONFIG:
        raise EbookBuildError(f"Unknown edition: {edition}")
    catalog = catalog or load_catalog(root / "papers" / "papers.json")
    guide_path = root / "humor-and-llms-field-guide.md"
    summaries_dir = root / "papers" / "summaries"

    guide = strip_guide_title(guide_path.read_text(encoding="utf-8"))
    guide = rewrite_relative_links(guide, guide_path)
    papers = summary_papers(catalog, summaries_dir)

    if edition == "guide":
        body = promote_guide_headings(guide)
    else:
        unavailable = [
            paper
            for paper in catalog["papers"]
            if paper.get("status") not in READY_STATUSES
        ]
        unavailable_note = ""
        if unavailable:
            labels = ", ".join(
                f"{paper['ref']} ({paper['title']})" for paper in unavailable
            )
            unavailable_note = (
                f" The cataloged source without a public summary is {labels}."
            )

        parts = [
            "# Part I — Field Guide {epub:type=part}",
            "",
            guide.rstrip(),
            "",
            "# Part II — Paper Summaries {epub:type=part}",
            "",
            (
                f"This companion contains {len(papers)} public summaries, grouped "
                "by catalog section and ordered within each section as recorded in "
                "the canonical catalog. Each summary is a research aid: begin with "
                "its limitations, then consult the linked primary source before "
                "citing a result."
                + unavailable_note
            ),
            "",
        ]
        for section, section_papers in sections_in_order(papers):
            parts.extend([f"## {section}", ""])
            for paper in section_papers:
                summary_path = summaries_dir / f"{paper['key']}.md"
                parts.extend([render_summary(paper, summary_path).rstrip(), ""])
        body = "\n".join(parts).rstrip() + "\n"

    body += "\n" + about_this_edition(edition, catalog, len(papers)).rstrip() + "\n"
    validate_public_manuscript(body)
    return markdown_metadata(edition, catalog, body) + body


def validate_public_manuscript(markdown: str) -> None:
    lowered = markdown.lower()
    found = [marker for marker in FORBIDDEN_PUBLIC_MARKERS if marker in lowered]
    if found:
        raise EbookBuildError(
            "Reader manuscript contains forbidden local/full-text markers: "
            + ", ".join(found)
        )

    relative_targets: list[str] = []
    for match in LINK_TARGET_RE.finditer(markdown):
        target = match.group("target")
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if not _is_external_or_internal_target(target):
            relative_targets.append(target)
    if relative_targets:
        raise EbookBuildError(
            "Reader manuscript contains relative links: "
            + ", ".join(sorted(set(relative_targets)))
        )


def resolve_executable(requested: str | None, default_name: str) -> str | None:
    candidate = requested or default_name
    resolved = shutil.which(candidate)
    if resolved:
        return resolved
    path = Path(candidate).expanduser()
    if path.is_file() and os.access(path, os.X_OK):
        return str(path.resolve())
    return None


def normalize_epub_archive(epub_path: Path, source_date: str) -> None:
    """Repack an EPUB with stable timestamps and compression.

    Pandoc records the wall-clock build time in ZIP entries.  Normalizing those
    entries makes repeat builds byte-for-byte stable for unchanged sources and
    tools while preserving the EPUB requirement that ``mimetype`` comes first
    and is stored without compression.
    """
    try:
        parsed_date = date.fromisoformat(source_date)
    except ValueError as error:
        raise EbookBuildError(
            f"Catalog update date is not ISO 8601: {source_date!r}"
        ) from error
    if parsed_date.year < 1980:
        raise EbookBuildError("EPUB archive dates must be 1980 or later")
    timestamp = (
        parsed_date.year,
        parsed_date.month,
        parsed_date.day,
        0,
        0,
        0,
    )
    normalized_path = epub_path.with_name(epub_path.stem + ".normalized.epub")
    try:
        with ZipFile(epub_path, "r") as source:
            infos = source.infolist()
            by_name = {info.filename: info for info in infos}
            if "mimetype" not in by_name:
                raise EbookBuildError(f"EPUB has no mimetype entry: {epub_path}")
            if source.read("mimetype") != b"application/epub+zip":
                raise EbookBuildError(f"EPUB has an invalid mimetype: {epub_path}")
            ordered = [by_name["mimetype"]] + [
                info for info in infos if info.filename != "mimetype"
            ]
            with ZipFile(normalized_path, "w") as destination:
                for info in ordered:
                    normalized = ZipInfo(info.filename, date_time=timestamp)
                    normalized.compress_type = (
                        ZIP_STORED if info.filename == "mimetype" else info.compress_type
                    )
                    normalized.comment = info.comment
                    normalized.internal_attr = info.internal_attr
                    normalized.external_attr = info.external_attr
                    normalized.create_system = info.create_system
                    normalized.create_version = info.create_version
                    normalized.extract_version = info.extract_version
                    compresslevel = (
                        9 if normalized.compress_type == ZIP_DEFLATED else None
                    )
                    payload = source.read(info.filename)
                    if info.filename.endswith(".opf"):
                        stable_modified = (
                            f"{source_date}T00:00:00Z".encode("ascii")
                        )
                        payload, replacements = DCTERMS_MODIFIED_RE.subn(
                            lambda match: (
                                match.group("prefix")
                                + stable_modified
                                + match.group("suffix")
                            ),
                            payload,
                        )
                        if replacements != 1:
                            raise EbookBuildError(
                                f"Expected one dcterms:modified value in {info.filename}; "
                                f"found {replacements}"
                            )
                    destination.writestr(
                        normalized,
                        payload,
                        compress_type=normalized.compress_type,
                        compresslevel=compresslevel,
                    )
        os.replace(normalized_path, epub_path)
    finally:
        normalized_path.unlink(missing_ok=True)


def run_epubcheck(epubcheck: str, epub_path: Path) -> None:
    result = subprocess.run(
        [epubcheck, str(epub_path)],
        text=True,
        capture_output=True,
        check=False,
    )
    output = "\n".join(
        chunk.strip() for chunk in (result.stdout, result.stderr) if chunk.strip()
    )
    if output:
        print(output)
    if result.returncode:
        raise EbookBuildError(
            f"EPUBCheck failed for {epub_path.name} with exit code {result.returncode}"
        )


def build_edition(
    edition: str,
    *,
    output_dir: Path,
    pandoc: str,
    epubcheck: str | None,
    require_epubcheck: bool,
) -> Path:
    catalog = load_catalog()
    manuscript = assemble_manuscript(edition, catalog=catalog)
    config = EDITION_CONFIG[edition]
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / str(config["filename"])

    with tempfile.TemporaryDirectory(prefix=".ebook-", dir=output_dir) as temporary:
        temporary_dir = Path(temporary)
        manuscript_path = temporary_dir / f"{edition}.md"
        candidate_path = temporary_dir / output_path.name
        manuscript_path.write_text(manuscript, encoding="utf-8")
        command = [
            pandoc,
            str(manuscript_path),
            "--from=markdown+smart",
            "--to=epub3",
            "--standalone",
            "--toc",
            f"--toc-depth={config['toc_depth']}",
            f"--split-level={config['split_level']}",
            f"--css={CSS_PATH}",
            "--wrap=none",
            f"--output={candidate_path}",
        ]
        result = subprocess.run(command, text=True, capture_output=True, check=False)
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.stderr.strip():
            print(result.stderr.strip(), file=sys.stderr)
        if result.returncode:
            raise EbookBuildError(
                f"Pandoc failed for {edition} with exit code {result.returncode}"
            )
        if not candidate_path.is_file() or candidate_path.stat().st_size == 0:
            raise EbookBuildError(f"Pandoc did not produce {candidate_path}")

        normalize_epub_archive(
            candidate_path,
            str(catalog.get("updated") or catalog.get("created") or ""),
        )

        if epubcheck:
            run_epubcheck(epubcheck, candidate_path)
        elif require_epubcheck:
            raise EbookBuildError(
                "EPUBCheck is required but was not found; install it or pass "
                "--epubcheck PATH"
            )
        else:
            print(
                "warning: EPUBCheck not found; structural validation was skipped",
                file=sys.stderr,
            )
        os.replace(candidate_path, output_path)

    size_kib = output_path.stat().st_size / 1024
    print(f"Wrote {output_path} ({size_kib:.1f} KiB)")
    return output_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--edition",
        choices=("guide", "complete", "all"),
        default="all",
        help="reader edition to build (default: both)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"output directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--pandoc",
        help="Pandoc executable name or path (default: search PATH)",
    )
    parser.add_argument(
        "--epubcheck",
        help="EPUBCheck executable name or path (default: search PATH)",
    )
    parser.add_argument(
        "--require-epubcheck",
        action="store_true",
        help="fail instead of warning when EPUBCheck is unavailable",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    pandoc = resolve_executable(args.pandoc, "pandoc")
    if not pandoc:
        print(
            "error: Pandoc was not found; install it or pass --pandoc PATH",
            file=sys.stderr,
        )
        return 2
    epubcheck = resolve_executable(args.epubcheck, "epubcheck")
    editions = tuple(EDITION_CONFIG) if args.edition == "all" else (args.edition,)
    try:
        for edition in editions:
            build_edition(
                edition,
                output_dir=args.output_dir.resolve(),
                pandoc=pandoc,
                epubcheck=epubcheck,
                require_epubcheck=args.require_epubcheck,
            )
    except (EbookBuildError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

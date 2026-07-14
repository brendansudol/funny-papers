"""Pure planning helpers for complete, page-bounded long-document extraction."""

from __future__ import annotations

import re
from pathlib import Path


UNIT_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_page_spec(spec: str) -> list[int]:
    """Expand a one-indexed page expression such as ``1-4,7,9-10``."""
    if not isinstance(spec, str) or not spec.strip():
        raise ValueError("page specification must be a non-empty string")
    pages: list[int] = []
    for part in spec.split(","):
        token = part.strip()
        if not token:
            raise ValueError(f"invalid page specification: {spec!r}")
        if "-" in token:
            bounds = token.split("-", 1)
            if len(bounds) != 2 or not all(bound.strip().isdigit() for bound in bounds):
                raise ValueError(f"invalid page range: {token!r}")
            start, end = (int(bound) for bound in bounds)
            if start < 1 or end < start:
                raise ValueError(f"invalid page range: {token!r}")
            pages.extend(range(start, end + 1))
        elif token.isdigit() and int(token) >= 1:
            pages.append(int(token))
        else:
            raise ValueError(f"invalid page number: {token!r}")
    if len(pages) != len(set(pages)):
        raise ValueError(f"duplicate page in specification: {spec!r}")
    return pages


def format_page_spec(pages: list[int]) -> str:
    if not pages:
        return ""
    runs: list[str] = []
    start = previous = pages[0]
    for page in pages[1:]:
        if page == previous + 1:
            previous = page
            continue
        runs.append(str(start) if start == previous else f"{start}-{previous}")
        start = previous = page
    runs.append(str(start) if start == previous else f"{start}-{previous}")
    return ",".join(runs)


def expected_page_count(paper: dict) -> int | None:
    restricted = paper.get("restricted_source", {}).get("page_count")
    return restricted or paper.get("page_count")


def validate_chapter_units(paper: dict) -> list[dict]:
    """Validate IDs, order, overlap, and complete physical-page coverage."""
    extraction = paper.get("extraction") or {}
    if extraction.get("strategy") != "chapters":
        raise ValueError(f"{paper['key']} is not configured for chapter extraction")
    raw_units = extraction.get("units")
    if not isinstance(raw_units, list) or not raw_units:
        raise ValueError(f"{paper['key']} needs at least one extraction unit")
    page_count = expected_page_count(paper)
    if not page_count:
        raise ValueError(f"{paper['key']} needs a source page count")

    units: list[dict] = []
    ids: set[str] = set()
    covered: list[int] = []
    next_page = 1
    for raw in raw_units:
        unit_id = raw.get("id")
        title = raw.get("title")
        if not isinstance(unit_id, str) or not UNIT_ID_RE.fullmatch(unit_id):
            raise ValueError(f"invalid extraction unit id: {unit_id!r}")
        if unit_id in ids:
            raise ValueError(f"duplicate extraction unit id: {unit_id}")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"{unit_id} needs a title")
        pages = parse_page_spec(raw.get("pages"))
        if pages != sorted(pages):
            raise ValueError(f"{unit_id} pages must be ordered")
        if pages[0] != next_page:
            raise ValueError(
                f"{unit_id} starts at page {pages[0]}; expected {next_page} for complete coverage"
            )
        if pages[-1] > page_count:
            raise ValueError(f"{unit_id} exceeds the {page_count}-page source")
        next_page = pages[-1] + 1
        covered.extend(pages)
        ids.add(unit_id)
        units.append({"id": unit_id, "title": title.strip(), "pages": pages})

    expected = list(range(1, page_count + 1))
    if covered != expected:
        missing = sorted(set(expected) - set(covered))
        overlap = len(covered) != len(set(covered))
        detail = f"missing pages {format_page_spec(missing)}" if missing else "page overlap"
        if overlap and missing:
            detail += " and page overlap"
        raise ValueError(f"{paper['key']} extraction units are incomplete: {detail}")
    return units


def page_file(pages_dir: Path, page: int) -> Path:
    return pages_dir / f"page_{page:04d}.md"


def missing_page_files(pages_dir: Path, page_count: int) -> list[int]:
    return [page for page in range(1, page_count + 1) if not page_file(pages_dir, page).is_file()]


def _page_fragment(page: int, text: str) -> str:
    return f"\n\n<!-- source-page-{page:04d} -->\n\n{text.strip()}"


def plan_chapter_inputs(paper: dict, pages_dir: Path, max_chars: int) -> list[dict]:
    """Load configured page files and split only at page boundaries if needed."""
    if max_chars < 1:
        raise ValueError("max_chars must be positive")
    units = validate_chapter_units(paper)
    page_count = expected_page_count(paper)
    assert page_count is not None
    missing = missing_page_files(pages_dir, page_count)
    if missing:
        raise FileNotFoundError(
            f"{paper['key']} is missing {len(missing)} page transcription(s): "
            f"{format_page_spec(missing)}"
        )

    planned: list[dict] = []
    for unit in units:
        chunks: list[tuple[list[int], str]] = []
        chunk_pages: list[int] = []
        fragments: list[str] = []
        length = 0
        for page in unit["pages"]:
            fragment = _page_fragment(
                page, page_file(pages_dir, page).read_text(encoding="utf-8")
            )
            if len(fragment) > max_chars:
                raise ValueError(
                    f"{paper['key']} page {page} alone exceeds the {max_chars:,}-character limit"
                )
            if fragments and length + len(fragment) > max_chars:
                chunks.append((chunk_pages, "".join(fragments).lstrip()))
                chunk_pages, fragments, length = [], [], 0
            chunk_pages.append(page)
            fragments.append(fragment)
            length += len(fragment)
        chunks.append((chunk_pages, "".join(fragments).lstrip()))

        for index, (pages, markdown) in enumerate(chunks, start=1):
            split = len(chunks) > 1
            planned.append(
                {
                    "id": f"{unit['id']}-part-{index}" if split else unit["id"],
                    "parent_id": unit["id"],
                    "title": (
                        f"{unit['title']} (part {index} of {len(chunks)})"
                        if split
                        else unit["title"]
                    ),
                    "pages": pages,
                    "page_spec": format_page_spec(pages),
                    "char_count": len(markdown),
                    "markdown": markdown,
                }
            )
    return planned

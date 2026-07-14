"""Resolve public and restricted paper sources without leaking private paths.

Restricted primary sources live below ``papers/private/``.  That directory is
gitignored as a unit; catalog entries deliberately record only publisher URLs,
coverage, and non-sensitive provenance such as page counts and hashes.
"""

from __future__ import annotations

from pathlib import Path


RESTRICTED_STATUS = "restricted"
RESTRICTED_NOTICE = (
    "Restricted primary source consulted; full text not distributed."
)


def is_restricted(paper: dict) -> bool:
    return paper.get("status") == RESTRICTED_STATUS


def private_paper_dir(root: Path, paper: dict) -> Path:
    return root / "papers" / "private" / paper["key"]


def paper_pdf_path(root: Path, paper: dict) -> Path:
    """Return the local PDF path while keeping it out of public metadata."""
    if is_restricted(paper):
        return private_paper_dir(root, paper) / "source.pdf"
    pdf_path = paper.get("pdf_path")
    if not pdf_path:
        raise ValueError(f"{paper['key']} has no PDF path")
    return root / pdf_path


def paper_md_dir(root: Path, paper: dict) -> Path:
    if is_restricted(paper):
        return private_paper_dir(root, paper) / "md"
    return root / "papers" / "md" / paper["key"]


def paper_md_path(root: Path, paper: dict) -> Path:
    """Return the combined transcription path for either access mode."""
    if is_restricted(paper):
        return paper_md_dir(root, paper) / f"{paper['key']}.md"
    md_path = paper.get("md_path")
    if md_path:
        return root / md_path
    # Downloaded papers do not acquire md_path until conversion succeeds.
    return paper_md_dir(root, paper) / f"{paper['key']}.md"


def paper_pages_dir(root: Path, paper: dict) -> Path:
    if is_restricted(paper):
        return paper_md_dir(root, paper) / "pages"
    pages_path = paper.get("md_pages_dir")
    if pages_path:
        return root / pages_path
    return paper_md_dir(root, paper) / "pages"


def conversion_progress_path(root: Path, paper: dict) -> Path:
    if is_restricted(paper):
        return private_paper_dir(root, paper) / "runs" / "conversion.progress.jsonl"
    return root / "papers" / "runs" / f"{paper['key']}.progress.jsonl"


def chapter_cache_dir(root: Path, paper: dict) -> Path:
    if not is_restricted(paper):
        raise ValueError("chapter intermediates are only supported for restricted sources")
    return private_paper_dir(root, paper) / "extraction" / "chapters"


def public_source_links(paper: dict) -> list[dict[str, object]]:
    """Return publisher links suitable for public Markdown.

    An entry may describe more than one primary work (T5 does).  ``consulted``
    remains attached so public views can distinguish covered from pending work.
    """
    links: list[dict[str, object]] = []
    seen: set[str] = set()
    for source in paper.get("official_sources", []):
        url = source.get("url")
        if not url or url in seen:
            continue
        links.append(
            {
                "label": source.get("label") or "publisher page",
                "url": url,
                "consulted": source.get("consulted"),
            }
        )
        seen.add(url)
    page_url = paper.get("page_url")
    if page_url and page_url not in seen:
        links.append({"label": "publisher page", "url": page_url, "consulted": None})
    return links


def access_notice(paper: dict) -> str:
    return paper.get("access_notice") or RESTRICTED_NOTICE


def analysis_ready(paper: dict, extracts_dir: Path) -> bool:
    """Whether a paper has a public extract that may enter generated analyses."""
    if paper.get("status") == "converted":
        return True
    return is_restricted(paper) and (extracts_dir / f"{paper['key']}.json").exists()

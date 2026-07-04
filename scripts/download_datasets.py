#!/usr/bin/env python3
"""Download every dataset listed in data/datasets.json.

Methods:
  git    -> shallow clone into data/<key>/ (records commit; LFS files come
            through as pointer stubs since git-lfs is not installed — these
            are detected and noted)
  hf     -> huggingface_hub.snapshot_download into data/<key>/ (no git-lfs
            needed)
  direct -> curl one or more URLs into data/<key>/

Size discipline: GitHub repos are pre-checked via the API and anything over
SIZE_CAP_MB is skipped with status "too_large" unless the entry sets
"allow_large": true. Everything is re-runnable; existing non-empty dataset
dirs are skipped.

Updates data/datasets.json in place with status / local_path / disk size /
commit. Run with the funny-papers venv:
  .venv/bin/python scripts/download_datasets.py [--only KEY]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "data" / "datasets.json"
DATA_DIR = ROOT / "data"

SIZE_CAP_MB = 2000
USER_AGENT = "funny-papers-dataset-fetcher/1.0"


def github_repo_size_mb(url: str) -> float | None:
    match = re.match(r"https://github\.com/([^/]+)/([^/]+?)(?:\.git|/.*)?$", url)
    if not match:
        return None
    owner, repo = match.group(1), match.group(2)
    api = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        req = urllib.request.Request(api, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as response:
            info = json.load(response)
        return info.get("size", 0) / 1024.0  # API reports KB
    except Exception:
        return None


def dir_size_mb(path: Path) -> float:
    total = sum(f.stat().st_size for f in path.rglob("*") if f.is_file())
    return total / (1024 * 1024)


def count_lfs_pointers(path: Path, limit: int = 5000) -> int:
    count = 0
    for i, f in enumerate(path.rglob("*")):
        if i > limit:
            break
        if f.is_file() and f.stat().st_size < 400:
            try:
                head = f.read_bytes()[:120]
            except OSError:
                continue
            if head.startswith(b"version https://git-lfs.github.com/spec"):
                count += 1
    return count


def fetch_git(entry: dict, dest: Path) -> dict:
    url = entry["source_url"]
    size_mb = github_repo_size_mb(url)
    if (
        size_mb is not None
        and size_mb > SIZE_CAP_MB
        and not entry.get("allow_large")
    ):
        return {
            "status": "too_large",
            "note_auto": f"GitHub reports ~{size_mb:.0f} MB > {SIZE_CAP_MB} MB cap; "
            "set allow_large=true to fetch anyway.",
        }
    subprocess.run(
        ["git", "clone", "--depth", "1", url, str(dest)],
        check=True,
        capture_output=True,
        text=True,
        timeout=1800,
    )
    commit = subprocess.run(
        ["git", "-C", str(dest), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
    ).stdout.strip()
    result = {"status": "downloaded", "commit": commit}
    pointers = count_lfs_pointers(dest)
    if pointers:
        result["note_auto"] = (
            f"{pointers} git-lfs pointer file(s) not materialized "
            "(git-lfs not installed); large binaries need `git lfs pull`."
        )
    return result


def fetch_hf(entry: dict, dest: Path) -> dict:
    from huggingface_hub import snapshot_download

    repo_id = entry.get("hf_repo_id")
    if not repo_id:
        match = re.match(
            r"https://huggingface\.co/datasets/([^/]+/[^/?#]+)", entry["source_url"]
        )
        if not match:
            return {"status": "failed", "note_auto": "Cannot parse HF repo id."}
        repo_id = match.group(1)
    snapshot_download(
        repo_id=repo_id,
        repo_type="dataset",
        local_dir=str(dest),
        max_workers=4,
    )
    return {"status": "downloaded"}


def fetch_direct(entry: dict, dest: Path) -> dict:
    urls = entry.get("direct_urls") or [entry["source_url"]]
    dest.mkdir(parents=True, exist_ok=True)
    for url in urls:
        filename = url.rstrip("/").split("/")[-1].split("?")[0] or "download"
        target = dest / filename
        subprocess.run(
            ["curl", "-sSL", "--fail", "--max-time", "900",
             "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
             "-o", str(target), url],
            check=True,
            timeout=960,
        )
    return {"status": "downloaded"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="Download only this dataset key")
    args = parser.parse_args()

    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    results = {"downloaded": 0, "skipped": 0, "failed": 0, "other": 0}

    for entry in catalog["datasets"]:
        key = entry["key"]
        if args.only and key != args.only:
            continue
        if entry.get("method") in (None, "unavailable"):
            results["other"] += 1
            continue
        if entry.get("status") in ("gated", "request", "too_large", "unavailable"):
            results["other"] += 1
            continue

        dest = DATA_DIR / key
        if dest.exists() and any(dest.iterdir()):
            if entry.get("status") != "downloaded":
                entry["status"] = "downloaded"
                entry["local_path"] = f"data/{key}"
                entry["disk_mb"] = round(dir_size_mb(dest), 1)
            results["skipped"] += 1
            continue

        print(f"[{key}] fetching via {entry['method']}: {entry['source_url']}", flush=True)
        try:
            if entry["method"] == "git":
                outcome = fetch_git(entry, dest)
            elif entry["method"] == "hf":
                outcome = fetch_hf(entry, dest)
            elif entry["method"] == "direct":
                outcome = fetch_direct(entry, dest)
            else:
                outcome = {"status": "failed", "note_auto": f"Unknown method {entry['method']}"}
        except subprocess.CalledProcessError as exc:
            stderr = (exc.stderr or "")[-500:] if hasattr(exc, "stderr") else ""
            outcome = {"status": "failed", "note_auto": f"{exc}. {stderr}".strip()}
        except Exception as exc:
            outcome = {"status": "failed", "note_auto": str(exc)[-500:]}

        entry.update(outcome)
        if outcome["status"] == "downloaded":
            entry["local_path"] = f"data/{key}"
            entry["disk_mb"] = round(dir_size_mb(dest), 1)
            results["downloaded"] += 1
            print(f"[{key}] ok ({entry['disk_mb']} MB)", flush=True)
        elif outcome["status"] == "too_large":
            results["other"] += 1
            print(f"[{key}] skipped: {outcome['note_auto']}", flush=True)
        else:
            results["failed"] += 1
            print(f"[{key}] FAILED: {outcome.get('note_auto', '')[:200]}", flush=True)

        CATALOG_PATH.write_text(
            json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

    print(
        f"\nDownloaded {results['downloaded']}, already present {results['skipped']}, "
        f"failed {results['failed']}, skipped/na {results['other']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

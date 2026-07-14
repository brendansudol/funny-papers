#!/usr/bin/env python3
"""Generate papers/ANALYSIS.md — cross-paper comparison views built from
papers/extracts/*.json.

Views:
  1. Datasets x papers (who introduced / evaluated on what)
  2. Models x papers (which models were actually run where)
  3. Humor theories x papers (operationalized vs motivation)
  4. Tasks x papers
  5. Headline results table (per dataset where possible)

Idempotent; rerun after extract_papers.py.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

try:
    from paper_sources import is_restricted
except ModuleNotFoundError:  # Imported as scripts.build_analysis in tests/tools.
    from scripts.paper_sources import is_restricted

ROOT = Path(__file__).resolve().parent.parent
EXTRACTS_DIR = ROOT / "papers" / "extracts"
PAPERS_PATH = ROOT / "papers" / "papers.json"
ANALYSIS_PATH = ROOT / "papers" / "ANALYSIS.md"

MIN_GROUP = 2  # only show dataset/model/task rows shared by >= this many papers


MODEL_ALIASES = {
    "bartlarge": "BART-Large",
    "baichuan27b": "Baichuan2-7B",
    "baseqwen7b": "Base Qwen-7B",
    "bertbase": "BERT-base",
    "chatgpt35": "GPT-3.5 Turbo",
    "chatglm36b": "ChatGLM3-6B",
    "deepseekr1": "DeepSeek-R1",
    "deepseekv3": "DeepSeek-V3",
    "gpt35": "GPT-3.5 Turbo",
    "gpt35turbo": "GPT-3.5 Turbo",
    "gpt3textdavinci002": "GPT-3 (text-davinci-002)",
    "gpt4turbo": "GPT-4 Turbo",
    "gpt4v": "GPT-4 Vision",
    "gpt4vision": "GPT-4 Vision",
    "gpt4o": "GPT-4o",
    "chatgpt4o": "GPT-4o",
    "gpt4omini": "GPT-4o mini",
    "gptoss120b": "gpt-oss-120B",
    "gemini15flash": "Gemini 1.5 Flash",
    "gemini15pro": "Gemini 1.5 Pro",
    "gemini20flash": "Gemini 2.0 Flash",
    "gemini20flashthinking": "Gemini 2.0 Flash Thinking",
    "gemini25flash": "Gemini 2.5 Flash",
    "gemini25flashlite": "Gemini 2.5 Flash-Lite",
    "gemini25pro": "Gemini 2.5 Pro",
    "gemini3pro": "Gemini 3 Pro",
    "gemma327b": "Gemma 3 27B",
    "grok3": "Grok 3",
    "claude3opus": "Claude 3 Opus",
    "claude35haiku": "Claude 3.5 Haiku",
    "claude35sonnet": "Claude 3.5 Sonnet",
    "claude37sonnet": "Claude 3.7 Sonnet",
    "claudeopus4": "Claude Opus 4",
    "claudesonnet4": "Claude Sonnet 4",
    "kimik2": "Kimi K2",
    "llama27b": "Llama-2-7B",
    "llama27bchat": "Llama-2-7B-Chat",
    "llama270b": "Llama-2-70B",
    "llama38b": "Llama-3-8B",
    "llama38binstruct": "Llama-3-8B-Instruct",
    "llama370b": "Llama-3-70B",
    "llama318b": "Llama-3.1-8B",
    "llama318binstruct": "Llama-3.1-8B-Instruct",
    "llama3370b": "Llama-3.3-70B",
    "o3mini": "OpenAI o3-mini",
    "openaio3mini": "OpenAI o3-mini",
    "mistral7b": "Mistral-7B",
    "mistral7binstruct": "Mistral-7B-Instruct",
    "minigpt4": "MiniGPT-4",
    "llava157b": "LLaVA-1.5-7B",
    "llava1513b": "LLaVA-1.5-13B",
    "qwen157b": "Qwen1.5-7B",
    "qwen215b": "Qwen2-1.5B",
    "qwen27b": "Qwen2-7B",
    "qwen257b": "Qwen2.5-7B",
    "qwen2572b": "Qwen2.5-72B",
    "qwen25omni7b": "Qwen2.5-Omni-7B",
    "qwen332b": "Qwen3-32B",
    "qwen2532binstruct": "Qwen2.5-32B-Instruct",
    "qwen2572binstruct": "Qwen2.5-72B-Instruct",
    "qwenplus": "Qwen-Plus",
    "qwenvlclot": "Qwen-VL+CLoT",
    "robertabase": "RoBERTa-base",
    "t5large": "T5-Large",
    "llama3370binstruct": "Llama-3.3-70B-Instruct",
}

TASK_ALIASES = {
    "ai-generated humor evaluation": "humor evaluation",
    "audience evaluation of ai-generated humor": "humor evaluation",
    "automated humor evaluation": "humor evaluation",
    "binary humor classification": "humor detection",
    "caption funniness ranking/evaluation": "humor evaluation",
    "caption ranking": "caption quality ranking",
    "cartoon caption generation": "humorous caption generation",
    "cartoon caption matching": "caption matching",
    "cartoon-caption humor explanation": "humor explanation",
    "culture-aware humorous captioning": "humorous caption generation",
    "funniness rating": "humor evaluation",
    "funniest response selection": "humor selection/ranking",
    "funny image caption generation": "humorous caption generation",
    "gif-based humorous caption generation": "humorous caption generation",
    "humor detection / humor discrimination": "humor detection",
    "humor detection": "humor detection",
    "humor evaluation": "humor evaluation",
    "humor explanation generation": "humor explanation",
    "humor interpretation / explanation": "humor explanation",
    "humor explanation": "humor explanation",
    "humor judgment": "humor evaluation",
    "humor preference evaluation": "humor evaluation",
    "humor preference selection": "humor selection/ranking",
    "humor production": "humor generation",
    "humor rating": "humor evaluation",
    "humor response ranking": "humor selection/ranking",
    "humor response selection": "humor selection/ranking",
    "humor scoring": "humor evaluation",
    "humor style recognition": "humor style classification",
    "humor style classification": "humor style classification",
    "humorous answer ranking": "humor selection/ranking",
    "humorous answer selection": "humor selection/ranking",
    "humorous cartoon caption generation": "humorous caption generation",
    "humorous image caption generation": "humorous caption generation",
    "humorous image captioning": "humorous caption generation",
    "joke creation": "humor generation",
    "joke detection / classification": "humor detection",
    "joke explanation": "humor explanation",
    "joke funniness assessment": "humor evaluation",
    "joke funniness evaluation": "humor evaluation",
    "joke generation": "humor generation",
    "joke quality evaluation": "humor evaluation",
    "joke ranking": "humor evaluation",
    "llm-as-a-judge humor evaluation": "humor evaluation",
    "llm-as-judge evaluation of jokes": "humor evaluation",
    "meme caption generation": "humorous caption generation",
    "multimodal humor explanation generation": "humor explanation",
    "natural language joke explanation": "humor explanation",
    "news-headline joke generation": "satirical headline generation",
    "pairwise humor evaluation": "humor evaluation",
    "pairwise humor preference judgment": "humor evaluation",
    "pairwise humor preference ranking": "humor evaluation",
    "pairwise joke comparison": "humor evaluation",
    "pairwise joke ranking": "humor evaluation",
    "pun explanation / rationale generation": "pun explanation",
    "pun interpretation/explanation": "pun explanation",
    "sarcasm classification": "sarcasm detection",
    "structured humor explanation": "humor explanation",
    "textual humor generation": "humor generation",
    "video humor explanation": "humor explanation",
    "wordplay translation": "pun translation",
    "zero-shot cartoon caption generation": "humorous caption generation",
}


def md_escape(text: str) -> str:
    return str(text).replace("|", "\\|")


def paper_link(extract: dict) -> str:
    key = extract["key"]
    return f"[{md_escape(extract['ref'])}](summaries/{key}.md)"


def normalize_model(name: str) -> str:
    """Canonicalize frequent spelling/version aliases without merging model families."""
    base = name.strip()
    base = re.sub(r"\s*\((?:20\d\d[-.\d]*|v[\d.]+|[\d-]+)\)$", "", base)
    base = re.sub(r"\s*\((?:gpt|gemini|claude)-[^)]+\)$", "", base, flags=re.I)
    base = re.sub(r"[-_ ]?20\d{2}[-.]\d{2}[-.]\d{2}$", "", base)
    key = re.sub(r"[^a-z0-9]+", "", base.lower())
    return MODEL_ALIASES.get(key, base)


def normalize_task(name: str) -> str:
    """Merge only broad task synonyms; retain meaningful subtask distinctions."""
    base = re.sub(r"\s+", " ", name.strip().lower().replace("humour", "humor"))
    return TASK_ALIASES.get(base, base)


def main() -> int:
    extracts = [
        json.loads(p.read_text(encoding="utf-8"))
        for p in sorted(EXTRACTS_DIR.glob("*.json"))
    ]
    if not extracts:
        print("No extracts found; run extract_papers.py first.")
        return 1
    catalog = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))["papers"]
    papers_by_key = {paper["key"]: paper for paper in catalog}
    restricted_count = sum(
        is_restricted(papers_by_key[extract["key"]])
        for extract in extracts
        if extract["key"] in papers_by_key
    )
    distributed_count = len(extracts) - restricted_count

    lines: list[str] = []
    lines.append("# Cross-Paper Analysis")
    lines.append("")
    lines.append(
        f"Comparison views over {len(extracts)} paper extracts. Regenerated "
        f"{date.today().isoformat()} by `scripts/build_analysis.py` from "
        f"[extracts/](extracts/) (primary-source-grounded: {distributed_count} "
        "distributed full texts"
        + (
            f" and {restricted_count} restricted sources whose full text is not distributed"
            if restricted_count
            else ""
        )
        + "; one JSON per paper). "
        f"One-page summaries: [summaries/](summaries/). "
        f"Methodological profiles and synthesis confidence: [EVIDENCE.md](EVIDENCE.md). "
        f"Common model spelling/version aliases and broad task synonyms are "
        f"normalized by the build script; source extracts remain unchanged. "
        f"Rows shared by fewer than {MIN_GROUP} papers are omitted from the "
        f"matrix views (see per-paper extracts for the long tail)."
    )
    lines.append("")

    # ---- 1. Datasets x papers ----
    dataset_rows: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for e in extracts:
        seen_datasets = set()
        for ds in e.get("datasets_used", []):
            key = (ds["name"], ds["role"])
            if key in seen_datasets:
                continue
            seen_datasets.add(key)
            dataset_rows[ds["name"]][ds["role"]].append(e)
    lines.append("## Datasets × papers")
    lines.append("")
    lines.append("| Dataset | Introduced by | Evaluated on by | Trained on by | Source/analyzed by |")
    lines.append("| --- | --- | --- | --- | --- |")
    for name, roles in sorted(
        dataset_rows.items(),
        key=lambda kv: -sum(len(v) for v in kv[1].values()),
    ):
        total = sum(len(v) for v in roles.values())
        if total < MIN_GROUP:
            continue
        def cell(*keys):
            papers = [p for k in keys for p in roles.get(k, [])]
            return ", ".join(paper_link(p) for p in papers) or "—"
        lines.append(
            f"| {md_escape(name)} | {cell('introduced')} | {cell('evaluated-on')} "
            f"| {cell('trained-on')} | {cell('source-material', 'analyzed')} |"
        )
    lines.append("")

    # ---- 2. Models x papers ----
    model_rows: dict[str, list] = defaultdict(list)
    for e in extracts:
        for m in set(normalize_model(m) for m in e.get("models_evaluated", [])):
            model_rows[m].append(e)
    lines.append("## Models × papers (models actually run)")
    lines.append("")
    lines.append("| Model | Papers evaluating it |")
    lines.append("| --- | --- |")
    for model, papers in sorted(model_rows.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
        if len(papers) < MIN_GROUP:
            continue
        lines.append(f"| {md_escape(model)} | {', '.join(paper_link(p) for p in papers)} |")
    lines.append("")

    # ---- 3. Humor theories x papers ----
    theory_rows: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for e in extracts:
        seen_theories = set()
        for t in e.get("humor_theories", []):
            if t["theory"] == "none":
                continue
            key = (t["theory"], t["usage"])
            if key in seen_theories:
                continue
            seen_theories.add(key)
            theory_rows[t["theory"]][t["usage"]].append(e)
    lines.append("## Humor theories × papers")
    lines.append("")
    lines.append("| Theory | Operationalized by | Grounding/motivation for | Cited in passing by |")
    lines.append("| --- | --- | --- | --- |")
    for theory, usages in sorted(
        theory_rows.items(), key=lambda kv: -sum(len(v) for v in kv[1].values())
    ):
        def tcell(key):
            return ", ".join(paper_link(p) for p in usages.get(key, [])) or "—"
        lines.append(
            f"| {md_escape(theory)} | {tcell('operationalized')} "
            f"| {tcell('grounding/motivation')} | {tcell('cited-in-passing')} |"
        )
    lines.append("")

    # ---- 4. Tasks x papers ----
    task_rows: dict[str, list] = defaultdict(list)
    for e in extracts:
        for t in set(normalize_task(t) for t in e.get("tasks", [])):
            task_rows[t].append(e)
    lines.append("## Tasks × papers")
    lines.append("")
    lines.append("| Task | Papers |")
    lines.append("| --- | --- |")
    for task, papers in sorted(task_rows.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if len(papers) < MIN_GROUP:
            continue
        lines.append(f"| {md_escape(task)} | {', '.join(paper_link(p) for p in papers)} |")
    lines.append("")

    # ---- 5. Headline results ----
    lines.append("## Headline results")
    lines.append("")
    lines.append(
        "Every extracted headline number, grouped by paper (see each extract "
        "for full context)."
    )
    lines.append("")
    lines.append("| Paper | Finding | Metric | Value | Dataset | Best system |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for e in extracts:
        for r in e.get("headline_results", []):
            lines.append(
                f"| {paper_link(e)} | {md_escape(r['finding'])} "
                f"| {md_escape(r.get('metric') or '—')} | {md_escape(r.get('value') or '—')} "
                f"| {md_escape(r.get('dataset') or '—')} | {md_escape(r.get('best_system') or '—')} |"
            )
    lines.append("")

    ANALYSIS_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {ANALYSIS_PATH} ({len(extracts)} extracts)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

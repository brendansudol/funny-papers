#!/usr/bin/env python3
"""Generate papers/EVIDENCE.md from enriched extracts and synthesis claims."""

from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path

try:
    from paper_sources import analysis_ready, is_restricted
except ModuleNotFoundError:  # Imported as scripts.build_evidence in tests/tools.
    from scripts.paper_sources import analysis_ready, is_restricted

ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = ROOT / "papers" / "papers.json"
EXTRACTS_DIR = ROOT / "papers" / "extracts"
CLAIMS_PATH = ROOT / "papers" / "synthesis_claims.json"
OUTPUT_PATH = ROOT / "papers" / "EVIDENCE.md"
CONFIDENCE_LEVELS = {"high", "moderate", "low", "insufficient"}


def md_escape(value) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def clipped(value: str, limit: int = 220) -> str:
    value = " ".join(str(value).split())
    return value if len(value) <= limit else value[: limit - 1].rstrip() + "…"


def paper_link(extract: dict) -> str:
    return f"[{md_escape(extract['ref'])}](summaries/{extract['key']}.md)"


def extract_link(extract: dict) -> str:
    return f"[{md_escape(extract['ref'])}](extracts/{extract['key']}.json)"


def joined(parts: list[str], limit: int | None = None) -> str:
    clean = [md_escape(part) for part in parts if part]
    if limit is not None and len(clean) > limit:
        remainder = len(clean) - limit
        clean = clean[:limit] + [f"+{remainder} more in JSON"]
    return "<br>".join(clean) or "—"


def format_humans(profile: dict) -> str:
    rows = []
    for sample in profile["human_samples"]:
        count = sample["participant_count"] or "n not reported"
        population = sample["population"] or "population not reported"
        row = f"{sample['role']}: {count}; {population}"
        if sample["observations"]:
            row += f"; observations: {sample['observations']}"
        rows.append(clipped(row))
    return joined(rows, 4) if rows else "None reported"


def format_judges(profile: dict) -> str:
    rows = []
    for judge in profile["judges"]:
        name = f" ({judge['name']})" if judge["name"] else ""
        blind = "blind" if judge["blind"] is True else "not blind" if judge["blind"] is False else "blinding NR"
        rows.append(f"{judge['type']}{name}; {judge['role']}; {blind}")
    return joined(rows, 6)


def format_baselines(profile: dict) -> str:
    rows = []
    for baseline in profile["human_baselines"]:
        if not baseline["present"]:
            rows.append(f"{baseline['scope']}: none")
            continue
        comparable = (
            "directly comparable"
            if baseline["directly_comparable"] is True
            else "not directly comparable"
            if baseline["directly_comparable"] is False
            else "comparability unclear"
        )
        rows.append(
            clipped(
                f"{baseline['scope']}: {baseline['description'] or 'present'}; {comparable}"
            )
        )
    return joined(rows, 4)


def format_dependence(profile: dict) -> str:
    dependence = profile["llm_judge_dependence"]
    detail = dependence["affected_claims"] or dependence["detail"]
    return f"**{dependence['level']}** — {md_escape(clipped(detail))}"


def format_selection(profile: dict) -> str:
    rows = []
    for selection in profile["generation_selection"]:
        n = f"; n={selection['n']}" if selection["n"] else ""
        selector = (
            f"; selector={selection['selector']}"
            if selection["selector"] not in {"none", "unclear"}
            else ""
        )
        rows.append(f"{selection['scope']}: {selection['mode']}{n}{selector}")
    return joined(rows, 4)


def format_models(profile: dict) -> str:
    rows = []
    for model in profile["model_provenance"]:
        provenance = []
        if model["version_or_snapshot"]:
            provenance.append(model["version_or_snapshot"])
        if model["inference_date"]:
            provenance.append(model["inference_date"])
        suffix = f" [{'; '.join(provenance)}]" if provenance else ""
        rows.append(f"{model['name']}{suffix}; {model['reporting']}")
    return joined(rows, 6) if rows else "No model run"


def format_budgets(profile: dict) -> str:
    rows = []
    for budget in profile["inference_budgets"]:
        fields = []
        for label, key in (
            ("calls", "calls_per_item"),
            ("candidates", "candidates_per_item"),
            ("tokens", "token_budget"),
            ("sampling", "sampling_parameters"),
            ("compute/cost", "compute_or_cost"),
        ):
            if budget[key]:
                fields.append(f"{label}: {budget[key]}")
        rows.append(clipped(f"{budget['scope']}: " + ("; ".join(fields) or budget["detail"])))
    return joined(rows, 3)


def format_contamination(profile: dict) -> str:
    risk = profile["contamination_risk"]
    return f"**{risk['level']}** — {md_escape(clipped(risk['basis']))}"


def format_gaps(profile: dict) -> str:
    return joined([clipped(gap, 140) for gap in profile["reporting_gaps"]], 5) or "None identified"


def validate_claims(claims: dict, paper_keys: set[str]) -> None:
    ids = [claim["id"] for claim in claims["claims"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate synthesis claim IDs")
    for claim in claims["claims"]:
        if claim["confidence"] not in CONFIDENCE_LEVELS:
            raise ValueError(f"{claim['id']}: invalid confidence {claim['confidence']}")
        for field in ("support", "counterevidence"):
            for citation in claim[field]:
                if citation["paper_key"] not in paper_keys:
                    raise ValueError(
                        f"{claim['id']}: unknown {field} paper {citation['paper_key']}"
                    )


def format_citations(citations: list[dict], extracts: dict[str, dict]) -> str:
    rows = []
    for citation in citations:
        extract = extracts[citation["paper_key"]]
        rows.append(f"{paper_link(extract)} {md_escape(citation['note'])}")
    return "<br>".join(rows) or "No direct counterevidence identified"


def main() -> int:
    catalog = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))["papers"]
    analysis_keys = {
        paper["key"] for paper in catalog if analysis_ready(paper, EXTRACTS_DIR)
    }
    extracts = {
        path.stem: json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(EXTRACTS_DIR.glob("*.json"))
    }
    missing = sorted(
        key for key in analysis_keys if not extracts.get(key, {}).get("evidence_profile")
    )
    if missing:
        raise ValueError(
            "Missing evidence profiles; run scripts/enrich_evidence.py: "
            + ", ".join(missing)
        )

    claims = json.loads(CLAIMS_PATH.read_text(encoding="utf-8"))
    validate_claims(claims, analysis_keys)
    profiles = [extracts[key]["evidence_profile"] for key in sorted(analysis_keys)]
    restricted_keys = {
        paper["key"]
        for paper in catalog
        if paper["key"] in analysis_keys and is_restricted(paper)
    }
    distributed_count = len(analysis_keys - restricted_keys)
    human_grounded = sum(bool(profile["human_samples"]) for profile in profiles)
    model_runs = sum(bool(profile["model_provenance"]) for profile in profiles)
    exact_versions = sum(
        any(model["reporting"] == "exact" for model in profile["model_provenance"])
        for profile in profiles
    )
    inference_dates = sum(
        any(model["inference_date"] for model in profile["model_provenance"])
        for profile in profiles
    )
    concrete_budgets = sum(
        any(
            any(
                budget[field]
                for field in (
                    "calls_per_item",
                    "candidates_per_item",
                    "token_budget",
                    "sampling_parameters",
                    "compute_or_cost",
                )
            )
            for budget in profile["inference_budgets"]
        )
        for profile in profiles
    )
    best_of_n = sum(
        any(item["mode"] in {"best-of-n", "both"} for item in profile["generation_selection"])
        for profile in profiles
    )
    human_baselines = sum(
        any(item["present"] for item in profile["human_baselines"])
        for profile in profiles
    )
    dependence = Counter(profile["llm_judge_dependence"]["level"] for profile in profiles)
    contamination = Counter(profile["contamination_risk"]["level"] for profile in profiles)

    lines = ["# Evidence Strength", ""]
    lines.append(
        f"Generated {date.today().isoformat()} from {len(analysis_keys)} primary-source-grounded "
        f"paper extracts ({distributed_count} distributed full texts"
        + (
            f"; {len(restricted_keys)} restricted primary sources whose full text is not distributed"
            if restricted_keys
            else ""
        )
        + ") plus the curated synthesis-claim map in "
        "[`synthesis_claims.json`](synthesis_claims.json). Evidence profiles separate "
        "participant counts from observations and preserve missing reporting instead of "
        "filling it by inference. Contamination risk and synthesis confidence are analyst "
        "assessments; all other profile fields are paper-reported facts."
    )
    lines.extend(
        [
            "",
            "## Confidence rubric",
            "",
            "- **High:** convergent evidence from multiple independent studies, including human-grounded evaluation, with counterevidence changing scope rather than reversing the claim.",
            "- **Moderate:** repeated or well-designed evidence, but important protocol, population, modality, or judge-dependence limitations remain.",
            "- **Low:** one or two narrow studies, weak human grounding, substantial LLM-judge dependence, or plausible conflicting results.",
            "- **Insufficient:** the library does not yet support a stable field-level conclusion.",
            "",
            "## Corpus audit",
            "",
            f"- **Human grounding:** {human_grounded} of {len(profiles)} papers report at least one human sample or participant population; {human_baselines} include at least one human baseline.",
            f"- **Model provenance:** {model_runs} papers run models; {exact_versions} report at least one exact model/checkpoint identifier and {inference_dates} report at least one inference or access date.",
            f"- **Inference and selection:** {concrete_budgets} papers report at least one concrete call, candidate, token, sampling, compute, or cost field; {best_of_n} use best-of-N selection in at least one experiment.",
            f"- **LLM-judge dependence:** {dependence['primary']} primary, {dependence['substantial']} substantial, {dependence['secondary']} secondary, {dependence['none']} none, and {dependence['unclear']} unclear.",
            "- **Contamination risk:** "
            + ", ".join(
                f"{level} {contamination[level]}"
                for level in ("high", "moderate", "low", "unclear", "not-applicable")
            )
            + ".",
            "",
            "## Synthesis claims",
            "",
            "| Claim | Support | Counterevidence / qualification | Confidence | Rationale |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for claim in claims["claims"]:
        lines.append(
            f"| **{claim['id']} — {md_escape(claim['claim'])}** "
            f"| {format_citations(claim['support'], extracts)} "
            f"| {format_citations(claim['counterevidence'], extracts)} "
            f"| **{claim['confidence']}** "
            f"| {md_escape(claim['rationale'])} |"
        )

    ordered_extracts = [extracts[p["key"]] for p in catalog if p["key"] in analysis_keys]
    lines.extend(
        [
            "",
            "## Human grounding and judgment",
            "",
            "Full details, including recruitment, geography, language, and observation counts, live in each linked extract.",
            "",
            "| Paper | Human sample / population | Judge types | Human baseline | LLM-judge dependence |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for extract in ordered_extracts:
        profile = extract["evidence_profile"]
        lines.append(
            f"| {extract_link(extract)} | {format_humans(profile)} | {format_judges(profile)} "
            f"| {format_baselines(profile)} | {format_dependence(profile)} |"
        )

    lines.extend(
        [
            "",
            "## Generation, provenance, and budget",
            "",
            "The Markdown view abbreviates long model lists; the linked JSON extract retains every reported model/version/date row.",
            "",
            "| Paper | Single-sample / best-of-N | Model version / date reporting | Inference budget | Contamination risk | Reporting gaps |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for extract in ordered_extracts:
        profile = extract["evidence_profile"]
        lines.append(
            f"| {extract_link(extract)} | {format_selection(profile)} | {format_models(profile)} "
            f"| {format_budgets(profile)} | {format_contamination(profile)} | {format_gaps(profile)} |"
        )

    OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} ({len(analysis_keys)} evidence profiles, {len(claims['claims'])} claims)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Shared schema and instructions for per-paper evidence profiles."""

from __future__ import annotations


EVIDENCE_PROFILE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "human_samples": {
            "type": "array",
            "description": "One row per distinct human participant or annotator population.",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "role": {
                        "type": "string",
                        "enum": [
                            "evaluation-participant",
                            "annotator",
                            "live-audience",
                            "content-creator",
                            "survey-respondent",
                            "dataset-contributor",
                            "other",
                        ],
                    },
                    "participant_count": {"type": ["string", "null"]},
                    "population": {"type": ["string", "null"]},
                    "recruitment": {"type": ["string", "null"]},
                    "geography": {"type": ["string", "null"]},
                    "languages": {"type": "array", "items": {"type": "string"}},
                    "observations": {
                        "type": ["string", "null"],
                        "description": "Ratings, votes, annotations, items, or performances; never present this as participant count.",
                    },
                    "detail": {"type": "string"},
                },
                "required": [
                    "role",
                    "participant_count",
                    "population",
                    "recruitment",
                    "geography",
                    "languages",
                    "observations",
                    "detail",
                ],
            },
        },
        "judges": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "type": {
                        "type": "string",
                        "enum": [
                            "human-lay",
                            "human-expert",
                            "human-crowd",
                            "live-audience",
                            "platform-vote",
                            "LLM",
                            "automatic-metric",
                            "author",
                            "none",
                        ],
                    },
                    "name": {"type": ["string", "null"]},
                    "role": {
                        "type": "string",
                        "enum": ["primary", "secondary", "validation", "data-labeling"],
                    },
                    "blind": {"type": ["boolean", "null"]},
                    "detail": {"type": "string"},
                },
                "required": ["type", "name", "role", "blind", "detail"],
            },
        },
        "generation_selection": {
            "type": "array",
            "minItems": 1,
            "description": "One row per generation experiment; use not-applicable for papers without generation.",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "scope": {"type": "string"},
                    "mode": {
                        "type": "string",
                        "enum": [
                            "single-sample",
                            "best-of-n",
                            "both",
                            "not-reported",
                            "not-applicable",
                        ],
                    },
                    "n": {"type": ["string", "null"]},
                    "selector": {
                        "type": "string",
                        "enum": [
                            "random",
                            "model-self-selection",
                            "LLM-judge",
                            "human",
                            "automatic-metric",
                            "rule",
                            "none",
                            "unclear",
                        ],
                    },
                    "detail": {"type": "string"},
                },
                "required": ["scope", "mode", "n", "selector", "detail"],
            },
        },
        "model_provenance": {
            "type": "array",
            "description": "Models actually run, preserving exact version, snapshot, and inference date when reported.",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "name": {"type": "string"},
                    "version_or_snapshot": {"type": ["string", "null"]},
                    "inference_date": {"type": ["string", "null"]},
                    "access": {
                        "type": "string",
                        "enum": ["API", "local", "hosted-service", "mixed", "unknown"],
                    },
                    "reporting": {
                        "type": "string",
                        "enum": ["exact", "partial", "family-only", "not-reported"],
                    },
                    "detail": {"type": ["string", "null"]},
                },
                "required": [
                    "name",
                    "version_or_snapshot",
                    "inference_date",
                    "access",
                    "reporting",
                    "detail",
                ],
            },
        },
        "inference_budgets": {
            "type": "array",
            "minItems": 1,
            "description": "One row per materially different inference setup; use nulls when not reported or not applicable.",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "scope": {"type": "string"},
                    "calls_per_item": {"type": ["string", "null"]},
                    "candidates_per_item": {"type": ["string", "null"]},
                    "token_budget": {"type": ["string", "null"]},
                    "sampling_parameters": {"type": ["string", "null"]},
                    "compute_or_cost": {"type": ["string", "null"]},
                    "detail": {"type": "string"},
                },
                "required": [
                    "scope",
                    "calls_per_item",
                    "candidates_per_item",
                    "token_budget",
                    "sampling_parameters",
                    "compute_or_cost",
                    "detail",
                ],
            },
        },
        "human_baselines": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "scope": {"type": "string"},
                    "present": {"type": "boolean"},
                    "description": {"type": ["string", "null"]},
                    "directly_comparable": {"type": ["boolean", "null"]},
                    "detail": {"type": "string"},
                },
                "required": [
                    "scope",
                    "present",
                    "description",
                    "directly_comparable",
                    "detail",
                ],
            },
        },
        "contamination_risk": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "level": {
                    "type": "string",
                    "enum": ["low", "moderate", "high", "unclear", "not-applicable"],
                },
                "paper_discusses": {"type": "boolean"},
                "benchmark_public_before_model": {"type": ["boolean", "null"]},
                "mitigations": {"type": "array", "items": {"type": "string"}},
                "basis": {"type": "string"},
            },
            "required": [
                "level",
                "paper_discusses",
                "benchmark_public_before_model",
                "mitigations",
                "basis",
            ],
        },
        "llm_judge_dependence": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "level": {
                    "type": "string",
                    "enum": ["none", "secondary", "substantial", "primary", "unclear"],
                },
                "affected_claims": {"type": ["string", "null"]},
                "human_validation": {"type": ["string", "null"]},
                "detail": {"type": "string"},
            },
            "required": ["level", "affected_claims", "human_validation", "detail"],
        },
        "reporting_gaps": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "human_samples",
        "judges",
        "generation_selection",
        "model_provenance",
        "inference_budgets",
        "human_baselines",
        "contamination_risk",
        "llm_judge_dependence",
        "reporting_gaps",
    ],
}


EVIDENCE_INSTRUCTIONS = """Evidence-profile rules:
- Human samples: distinguish participant counts from numbers of ratings, votes, items, or annotations. Never infer one from the other. Preserve exact qualifiers such as "at least," "per language," or exclusions.
- Judges: record every source that determines a result or label. An LLM used as a metric or evaluator is an LLM judge even if the paper calls it an automatic metric.
- Generation selection: distinguish one sampled output from best-of-N generation followed by selection. Repeated evaluation or majority voting over a fixed output is not best-of-N.
- Model provenance: record only models actually run. Preserve exact API snapshot/version and inference/access dates when stated; use null rather than guessing.
- Inference budget: capture calls, candidates, token limits, sampling parameters, compute, and cost exactly when stated. Missing reporting is itself evidence and belongs in reporting_gaps.
- Human baseline: mark directly_comparable true only when human and model outputs or performance were evaluated under materially matched conditions.
- Contamination risk: this is a conservative analyst assessment. Separate controls stated by the paper from uncertainty. Public legacy benchmarks evaluated with later proprietary models normally remain at least moderate risk unless the design uses held-out/private/newly created items or a convincing decontamination test.
- LLM-judge dependence: "primary" means the headline conclusion rests mainly on LLM judgments; "substantial" means important conclusions do; "secondary" means LLM judging is corroborative or diagnostic; "none" means it does not determine the conclusions.
- For non-empirical papers, use empty human/model arrays and explicit not-applicable/none rows rather than inventing a study design.
"""

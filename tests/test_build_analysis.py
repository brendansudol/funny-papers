import glob
import json
import re
import unittest
from collections import defaultdict
from pathlib import Path

from scripts.build_analysis import normalize_model, normalize_task


class AnalysisNormalizationTest(unittest.TestCase):
    def test_model_aliases_group_spelling_and_release_variants(self):
        self.assertEqual(normalize_model("Gemini-2.5-Pro"), "Gemini 2.5 Pro")
        self.assertEqual(normalize_model("Gemini 2.5 Pro"), "Gemini 2.5 Pro")
        self.assertEqual(normalize_model("GPT-4o-mini"), "GPT-4o mini")
        self.assertEqual(normalize_model("GPT-4o mini"), "GPT-4o mini")
        self.assertEqual(
            normalize_model("GPT-4o (gpt-4o-2024-08-06)"), "GPT-4o"
        )
        self.assertEqual(normalize_model("GPT OSS 120B"), "gpt-oss-120B")
        self.assertEqual(normalize_model("gpt-oss-120B"), "gpt-oss-120B")
        self.assertEqual(normalize_model("LLaMA2-7B"), "Llama-2-7B")
        self.assertEqual(normalize_model("Llama-2-7b"), "Llama-2-7B")
        self.assertEqual(normalize_model("T5-large"), "T5-Large")
        self.assertEqual(normalize_model("Qwen 2.5-72B"), "Qwen2.5-72B")

    def test_task_aliases_merge_only_broad_synonyms(self):
        self.assertEqual(normalize_task("humour generation"), "humor generation")
        self.assertEqual(normalize_task("joke generation"), "humor generation")
        self.assertEqual(normalize_task("joke explanation"), "humor explanation")
        self.assertEqual(
            normalize_task("humour style recognition"),
            "humor style classification",
        )
        self.assertEqual(normalize_task("pun generation"), "pun generation")
        self.assertEqual(normalize_task("funniness rating"), "humor evaluation")
        self.assertEqual(
            normalize_task("joke funniness evaluation"), "humor evaluation"
        )
        self.assertEqual(
            normalize_task("humorous image caption generation"),
            "humorous caption generation",
        )
        self.assertEqual(normalize_task("pun explanation"), "pun explanation")

    def test_current_extracts_have_no_compact_label_collisions(self):
        for field, normalizer in (
            ("models_evaluated", normalize_model),
            ("tasks", normalize_task),
        ):
            groups = defaultdict(set)
            for path in glob.glob("papers/extracts/*.json"):
                extract = json.loads(Path(path).read_text())
                for raw in extract.get(field, []):
                    normalized = normalizer(raw)
                    compact = re.sub(r"[^a-z0-9]+", "", normalized.lower())
                    groups[compact].add(normalized)
            collisions = [sorted(values) for values in groups.values() if len(values) > 1]
            self.assertEqual(collisions, [], field)


if __name__ == "__main__":
    unittest.main()

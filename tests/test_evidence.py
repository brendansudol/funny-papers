import json
import unittest
from pathlib import Path

from scripts.build_evidence import validate_claims
from scripts.evidence_schema import EVIDENCE_PROFILE_SCHEMA


ROOT = Path(__file__).resolve().parent.parent


class EvidenceLayerTest(unittest.TestCase):
    def test_all_converted_papers_have_complete_profiles(self):
        papers = json.loads((ROOT / "papers/papers.json").read_text())["papers"]
        converted = [paper for paper in papers if paper["status"] == "converted"]
        required = set(EVIDENCE_PROFILE_SCHEMA["required"])
        contamination_levels = {"low", "moderate", "high", "unclear", "not-applicable"}
        dependence_levels = {"none", "secondary", "substantial", "primary", "unclear"}

        self.assertEqual(len(converted), 107)
        for paper in converted:
            path = ROOT / f"papers/extracts/{paper['key']}.json"
            extract = json.loads(path.read_text())
            self.assertTrue(
                extract.get("evidence_enriched_at") or extract.get("extracted_at"),
                paper["key"],
            )
            profile = extract.get("evidence_profile")
            self.assertIsInstance(profile, dict, paper["key"])
            self.assertEqual(required, set(profile), paper["key"])
            self.assertTrue(profile["judges"], paper["key"])
            self.assertTrue(profile["generation_selection"], paper["key"])
            self.assertTrue(profile["inference_budgets"], paper["key"])
            self.assertTrue(profile["human_baselines"], paper["key"])
            self.assertIn(profile["contamination_risk"]["level"], contamination_levels)
            self.assertIn(profile["llm_judge_dependence"]["level"], dependence_levels)

    def test_synthesis_claims_reference_cataloged_papers(self):
        papers = json.loads((ROOT / "papers/papers.json").read_text())["papers"]
        claims = json.loads((ROOT / "papers/synthesis_claims.json").read_text())
        validate_claims(claims, {paper["key"] for paper in papers})
        self.assertEqual(len(claims["claims"]), 11)


if __name__ == "__main__":
    unittest.main()

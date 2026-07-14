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

        self.assertEqual(len(converted), 111)
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

    def test_guide_certification_covers_every_converted_entry(self):
        papers = json.loads((ROOT / "papers/papers.json").read_text())["papers"]
        converted = {paper["key"] for paper in papers if paper["status"] == "converted"}
        historical = json.loads(
            (ROOT / "papers/review/discrepancies.json").read_text()
        )
        certification = json.loads(
            (ROOT / "papers/review/certification.json").read_text()
        )

        historical_keys = {result["key"] for result in historical["results"]}
        second_pass = certification["guide_audit"]
        second_pass_keys = {result["key"] for result in second_pass["results"]}

        self.assertEqual(len(historical_keys), 80)
        self.assertEqual(len(second_pass_keys), 31)
        self.assertTrue(historical_keys.isdisjoint(second_pass_keys))
        self.assertEqual(converted, historical_keys | second_pass_keys)
        self.assertEqual(
            second_pass["claims_checked"],
            sum(result["claims_checked"] for result in second_pass["results"]),
        )

        combined = certification["combined_guide_coverage"]
        self.assertEqual(combined["converted_entries_checked"], len(converted))
        self.assertEqual(combined["converted_entries_total"], len(converted))
        self.assertEqual(
            combined["claims_checked"],
            historical["claims_checked"] + second_pass["claims_checked"],
        )

    def test_extract_spot_check_is_well_formed(self):
        certification = json.loads(
            (ROOT / "papers/review/certification.json").read_text()
        )
        audit = certification["extract_audit"]
        results = audit["results"]
        keys = [result["key"] for result in results]

        self.assertEqual(audit["sample_size"], 26)
        self.assertEqual(len(keys), audit["sample_size"])
        self.assertEqual(len(keys), len(set(keys)))
        self.assertTrue(all(result["status"] == "passed" for result in results))
        self.assertEqual(audit["outcome"]["passed"], len(results))
        for key in keys:
            self.assertTrue((ROOT / f"papers/extracts/{key}.json").exists(), key)


if __name__ == "__main__":
    unittest.main()

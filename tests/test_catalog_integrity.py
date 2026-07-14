import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class CatalogIntegrityTest(unittest.TestCase):
    def test_paper_catalog_uses_canonical_tags_and_sections(self):
        papers = json.loads((ROOT / "papers/papers.json").read_text())["papers"]
        canonical_tags = {
            "theory",
            "peer-reviewed",
            "preprint",
            "workshop",
            "dataset",
            "method",
            "benchmark",
            "HCI study",
            "evaluation study",
            "shared task",
            "survey",
        }
        tags = {tag for paper in papers for tag in paper.get("tags", [])}
        sections = {paper["section"] for paper in papers}

        self.assertEqual(len(papers), 116)
        self.assertLessEqual(tags, canonical_tags)
        self.assertNotIn("evaluation-study", tags)
        self.assertNotIn("shared-task", tags)
        self.assertEqual(
            {section for section in sections if section.startswith("Part 4")},
            {"Part 4 - Evaluation Methodology"},
        )
        self.assertEqual(
            {section for section in sections if section.startswith("Part 5")},
            {"Part 5 - Situated & Live Humor"},
        )

    def test_dataset_catalog_cardinality(self):
        datasets = json.loads((ROOT / "data/datasets.json").read_text())["datasets"]
        downloaded = [dataset for dataset in datasets if dataset["status"] == "downloaded"]

        self.assertEqual(len(datasets), 53)
        self.assertEqual(len(downloaded), 39)


if __name__ == "__main__":
    unittest.main()

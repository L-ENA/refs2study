import tempfile
import unittest
from pathlib import Path

from refs2study.io import load_gold_standard_csv


class TestGoldStandardLoading(unittest.TestCase):
    def test_load_gold_standard_csv_returns_references(self) -> None:
        csv_content = """study_id,reference_id,type,volume,source,city,conferenceName,edition,editor,publisher,bookName,date,allAuthors,issue,journalName,originalTitle,pages
study-1,ref-1,Journal article,10,Source A,London,Conf A,2,Ed A,Pub A,Book A,2024,Author A,1,Journal A,Title A,1-10
study-1,ref-2,Journal article,11,Source B,Paris,Conf B,1,Ed B,Pub B,Book B,2024,Author B,2,Journal B,Title B,11-20
"""
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "gold.csv"
            csv_path.write_text(csv_content, encoding="utf-8")

            references = load_gold_standard_csv(csv_path)

        self.assertEqual(len(references), 2)
        self.assertEqual(references[0].study_id, "study-1")
        self.assertEqual(references[0].reference_id, "ref-1")
        self.assertEqual(references[0].originalTitle, "Title A")


if __name__ == "__main__":
    unittest.main()

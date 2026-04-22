import unittest

from refs2study.evaluation import clusters_to_duplicate_pairs, evaluate_duplicates


class TestEvaluation(unittest.TestCase):
    def test_evaluate_duplicates_matches_expected_precision_and_recall(self) -> None:
        predicted = {"cluster-1": ["a", "b"], "cluster-2": ["c", "d"]}
        gold = {"study-1": ["a", "b"], "study-2": ["c", "e"]}

        found_dupes = clusters_to_duplicate_pairs(predicted)
        true_dupes = clusters_to_duplicate_pairs(gold)
        result = evaluate_duplicates(found_dupes, true_dupes)

        self.assertEqual(result["found_duplicates"], 2)
        self.assertEqual(result["true_positives"], 1)
        self.assertEqual(result["precision"], 0.5)
        self.assertEqual(result["recall"], 0.5)


if __name__ == "__main__":
    unittest.main()

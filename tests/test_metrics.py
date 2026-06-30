import unittest

from src.metrics import attachment_scores


class AttachmentScoresTest(unittest.TestCase):
    def test_exact_match_scores_one(self):
        scores = attachment_scores(
            gold_heads=[-1, 2, 0, 2],
            predicted_heads=[-1, 2, 0, 2],
            gold_labels=["ROOT", "obl", "root", "amod"],
            predicted_labels=["ROOT", "obl", "root", "amod"],
            ignore_indices={0},
        )
        self.assertEqual(scores["token_count"], 3)
        self.assertEqual(scores["UAS"], 1.0)
        self.assertEqual(scores["LAS"], 1.0)

    def test_label_error_only_lowers_las(self):
        scores = attachment_scores(
            gold_heads=[-1, 2, 0, 2],
            predicted_heads=[-1, 2, 0, 2],
            gold_labels=["ROOT", "obl", "root", "amod"],
            predicted_labels=["ROOT", "obj", "root", "amod"],
            ignore_indices={0},
        )
        self.assertEqual(scores["token_count"], 3)
        self.assertEqual(scores["UAS"], 1.0)
        self.assertAlmostEqual(scores["LAS"], 2 / 3)

    def test_head_error_lowers_both_scores(self):
        scores = attachment_scores(
            gold_heads=[-1, 2, 0, 2],
            predicted_heads=[-1, 0, 0, 2],
            gold_labels=["ROOT", "obl", "root", "amod"],
            predicted_labels=["ROOT", "obl", "root", "amod"],
            ignore_indices={0},
        )
        self.assertEqual(scores["token_count"], 3)
        self.assertAlmostEqual(scores["UAS"], 2 / 3)
        self.assertAlmostEqual(scores["LAS"], 2 / 3)

    def test_length_mismatch_raises(self):
        with self.assertRaises(ValueError):
            attachment_scores([0], [0, 1], ["root"], ["root"])


if __name__ == "__main__":
    unittest.main()

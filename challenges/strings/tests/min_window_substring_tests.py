from unittest import TestCase
from min_window_substring import MinWindowSubstring


class MinWindowSubstringTests(TestCase):
    def setUp(self):
        self.cases = [
            (["aaabaaddae", "aed"], "dae"),
            (["aabdccdbcacd", "aad"], "aabd"),
            (["aaaaaaaaa", "a"], "a"),
            (["aaffsfsfasfasfasfasfasfacasfafe", "fafe"], "fafe"),
            (["aaffsfsfasfasfasfasfasfacasfafe", "fafsf"], "affsf"),
            (["vvavereveaevafefaef", "vvev"], "vvave"),
            (["caae", "cae"], "caae"),
            (["cccaabbbbrr", "rbac"], "caabbbbr"),
        ]

    def test__substring_at_the_end(self):
        self.assertEqual(MinWindowSubstring(["aaabaaddae", "aed"]), "dae")

    def test__substring_at_the_beginning(self):
        self.assertEqual(MinWindowSubstring(["aabdccdbcacd", "aad"]), "aabd")

    def test__single_letter_substring_and_multiple_duped_master(self):
        self.assertEqual(MinWindowSubstring(["aaaaaaaaa", "a"]), "a")

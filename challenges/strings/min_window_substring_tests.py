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

    def test__run_cases(self):
        pass

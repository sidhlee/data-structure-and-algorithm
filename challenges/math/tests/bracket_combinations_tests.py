from unittest import TestCase
from challenges.math.bracket_combinations import bracket_combinations


class BracketCombinationsTests(TestCase):
    def setUp(self):
        self.test_cases = [
            (1, 1),
            (2, 2),
            (3, 5),
            (4, 14),
            (5, 42),
            (6, 132),
            (7, 429),
            (8, 1430),
            (9, 4862),
        ]

    def test__success(self):
        for case, expected in self.test_cases:
            self.assertEqual(bracket_combinations(case), expected)

    def test__zero(self):
        self.assertEqual(bracket_combinations(0), 1)

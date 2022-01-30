import unittest
from multiple_pointers_pattern import sum_zero


class SumZeroTestCase(unittest.TestCase):
    def test_returns_first_pair_where_sum_is_zero(self):
        self.assertEqual(sum_zero([-3, -2, -1, 0, 1, 2, 3]), [-3, 3])

    def test_pair_not_found(self):
        self.assertIsNone(sum_zero([-2, 0, 1, 3]))
        self.assertIsNone(sum_zero([1, 2, 3]))

    def test_one_zero(self):
        self.assertIsNone(sum_zero([0]))

    def test_two_zeros(self):
        self.assertEqual(sum_zero([0, 0]), [0, 0])

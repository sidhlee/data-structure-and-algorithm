import unittest
from sliding_window_pattern import max_subarray_sum


class MaxSubarraySumTestCase(unittest.TestCase):
    def test_success(self):
        array = [1, 2, 5, 2, 8, 1, 5]
        self.assertEqual(max_subarray_sum(array, 2), 10)
        self.assertEqual(max_subarray_sum(array, 4), 17)
        self.assertEqual(max_subarray_sum(array, 1), 8)

    def test_empty_array_returns_none(self):
        self.assertIsNone(max_subarray_sum([], 4))

    def test_subarray_bigger_than_array(self):
        self.assertIsNone(max_subarray_sum([1, 2], 3))

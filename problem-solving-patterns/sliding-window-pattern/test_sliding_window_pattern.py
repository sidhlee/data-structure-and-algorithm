import unittest
from sliding_window_pattern import (
    max_subarray_sum,
    min_subarray_len,
    find_longest_substring,
)


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


class MinSubarrayLenTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(min_subarray_len([2, 3, 1, 2, 4, 3], 7), 2)
        self.assertEqual(min_subarray_len([2, 1, 6, 5, 4], 9), 2)
        self.assertEqual(
            min_subarray_len([3, 1, 7, 11, 2, 9, 8, 21, 62, 33, 19], 52), 1
        )
        self.assertEqual(min_subarray_len([4, 3, 3, 8, 1, 2, 3], 11), 2)
        self.assertEqual(min_subarray_len([1, 4, 16, 22, 5, 7, 8, 9, 10], 39), 3)
        self.assertEqual(min_subarray_len([1, 4, 16, 22, 5, 7, 8, 9, 10], 55), 5)

    def test_no_min_subarray(self):
        self.assertEqual(min_subarray_len([1, 4, 16, 22, 5, 7, 8, 9, 10], 95), 0)


class FindLongestSubstringTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(find_longest_substring("thisisawesome"), 6)
        self.assertEqual(find_longest_substring("thecatinthehat"), 7)
        self.assertEqual(find_longest_substring("longestsubstring"), 8)
        self.assertEqual(find_longest_substring("thisishowwedoit"), 6)

    def test_empty_string(self):
        self.assertEqual(find_longest_substring(""), 0)

    def test_duplicated_letters(self):
        self.assertEqual(find_longest_substring("bbb"), 1)

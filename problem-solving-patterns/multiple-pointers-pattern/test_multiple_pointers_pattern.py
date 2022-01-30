import unittest
from multiple_pointers_pattern import (
    sum_zero,
    count_unique_values,
    are_there_duplicates,
    average_pair,
    is_subsequence,
)


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


class CountUniqueValues(unittest.TestCase):
    def test_success(self):
        self.assertEqual(count_unique_values([1, 1, 1, 1, 1, 2]), 2)
        self.assertEqual(count_unique_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]), 7)
        self.assertEqual(count_unique_values([-2, -1, -1, 0, 1]), 4)

    def test_empty_list(self):
        self.assertEqual(count_unique_values([]), 0)


class AreThereDuplicatesTestCase(unittest.TestCase):
    def test_number_duplicates(self):
        self.assertTrue(are_there_duplicates(1, 2, 2))

    def test_string_duplicates(self):
        self.assertTrue(are_there_duplicates("a", "b", "c", "a"))

    def test_no_duplicates(self):
        self.assertFalse(are_there_duplicates(1, 2, 3))


class AveragePairTestCase(unittest.TestCase):
    def test_found_pair(self):
        self.assertTrue(average_pair([1, 2, 3], 2.5))
        self.assertTrue(average_pair([1, 3, 3, 5, 6, 7, 10, 12, 19], 8))

    def test_no_pair(self):
        self.assertFalse(average_pair([-1, 0, 3, 4, 5, 6], 4.1))

    def test_empty_list(self):
        self.assertFalse(average_pair([], 4))

    def test_one_integer(self):
        self.assertFalse(average_pair([1], 1))

    def test_two_same_integers(self):
        self.assertTrue(average_pair([1, 1], 1))


class IsSubsequenceTestCase(unittest.TestCase):
    def test_str1_in_str2(self):
        self.assertTrue(is_subsequence("hello", "hello world"))

    def test_inserted_characters(self):
        self.assertTrue(is_subsequence("sing", "sting"))
        self.assertTrue(is_subsequence("abc", "abracadabra"))

    def test_character_order_changed(self):
        self.assertFalse(is_subsequence("abc", "acb"))

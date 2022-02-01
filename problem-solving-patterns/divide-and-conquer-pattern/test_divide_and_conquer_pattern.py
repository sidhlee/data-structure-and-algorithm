import unittest
from divide_and_conquer_pattern import binary_search_recursive, binary_search_iterative


class BinarySearchRecursiveTestCase(unittest.TestCase):
    def test_value_in_the_middle(self):
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5, 6], 4), 3)

    def test_value_at_the_end(self):
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5, 6], 6), 5)

    def test_value_not_found(self):
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5, 6], 7), -1)

    def test_single_value(self):
        self.assertEqual(binary_search_recursive([1], 1), 0)


class BinarySearchIterativeTestCase(unittest.TestCase):
    def test_value_in_the_middle(self):
        self.assertEqual(binary_search_iterative([1, 2, 3, 4, 5, 6], 4), 3)

    def test_value_at_the_end(self):
        self.assertEqual(binary_search_iterative([1, 2, 3, 4, 5, 6], 6), 5)

    def test_value_not_found(self):
        self.assertEqual(binary_search_iterative([1, 2, 3, 4, 5, 6], 7), -1)

    def test_single_value(self):
        self.assertEqual(binary_search_iterative([1], 1), 0)

import unittest
from searching_algorithms import linear_search, binary_search, naive_string_search


class LinearSearchTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(linear_search([3, 1, 2], 1), 1)

    def test_not_found(self):
        self.assertEqual(linear_search([3, 1, 2], 4), -1)


class BinarySearchTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 7), 6)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 4), 3)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6], 3), 2)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 2, 3], 4), -1)


class NaiveStringSearch(unittest.TestCase):
    def test_success(self):
        self.assertEqual(
            naive_string_search("This is very slow naive string search", "is"), 2
        )

import unittest
from utils.time import time_func
from sorting_algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    compare_and_sort,
    merge_sort,
    pivot,
    quick_sort,
    radix_sort,
    flatten,
    get_num_digits,
    get_max_digits,
    get_ith_digit,
)


class BubbleSortTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(bubble_sort([5, 2, 8, -3, 0, -65]), [-65, -3, 0, 2, 5, 8])

    def test_faster_with_almost_sorted_array(self):
        sorted_numbers = [i for i in range(1000)]
        reverse_sorted_numbers = sorted_numbers.copy()
        reverse_sorted_numbers.reverse()

        sorted_delta, sorted_result = time_func(lambda: bubble_sort(sorted_numbers))
        reverse_delta, reverse_result = time_func(
            lambda: bubble_sort(reverse_sorted_numbers)
        )

        self.assertLess(sorted_delta, reverse_delta / 2)
        self.assertEqual(sorted_result, reverse_result)


class SelectionSortTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(selection_sort([5, 2, 8, -3, 0, -65]), [-65, -3, 0, 2, 5, 8])


class InsertionSortTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(insertion_sort([5, 2, 8, -3, 0, -65]), [-65, -3, 0, 2, 5, 8])

    def test_appending_item(self):
        reverse_sorted_numbers = [1000 - i for i in range(1000)]
        delta, result = time_func(lambda: insertion_sort(reverse_sorted_numbers))
        new_array = [*result, -100]
        new_delta, new_result = time_func(lambda: insertion_sort(new_array))
        self.assertLess(new_delta, delta / 2)
        self.assertEqual(new_result, [-100, *result])


class CompareAndSortTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(
            compare_and_sort([1, 4, 7], [2, 3, 8, 12]), [1, 2, 3, 4, 7, 8, 12]
        )
        self.assertEqual(
            compare_and_sort([1, 2, 5], [-65, -3, 0, 8]), [-65, -3, 0, 1, 2, 5, 8]
        )

    def test_one_empty_array(self):
        self.assertEqual(compare_and_sort([], [2, 3, 8, 12]), [2, 3, 8, 12])

    def test_single_item_arrays(self):
        self.assertEqual(compare_and_sort([1], [0]), [0, 1])


class MergeSortTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(merge_sort([1, 5, 2, 8, -3, 0, -65]), [-65, -3, 0, 1, 2, 5, 8])


class PivotTestCase(unittest.TestCase):
    def test_returns_pivot_index(self):
        self.assertEqual(pivot([5, 2, 4, 1, 13, 8]), 3)

    def test_reorganizes_items(self):
        arr = [3, 2, 1]
        pivot(arr)
        self.assertEqual(arr, [1, 2, 3])

    def test_smaller_values_to_the_left(self):
        arr = [5, 2, 13, 1, 4, 8]
        pivot_index = pivot(arr)
        pivot_value = arr[pivot_index]
        left_values = arr[0:pivot_index]
        self.assertTrue(all([item < pivot_value for item in left_values]))

    def test_greater_values_to_the_right(self):
        arr = [5, 2, 13, 1, 4, 8]
        pivot_index = pivot(arr)
        pivot_value = arr[pivot_index]
        right_values = arr[pivot_index + 1 :]
        self.assertTrue(all([pivot_value < item for item in right_values]))

    def test_duplicated_values(self):
        arr = [3, 2, 1, 3, 2, 1]
        self.assertEqual(pivot(arr), 4)
        self.assertEqual(arr, [1, 2, 1, 2, 3, 3])


class QuickSortTestCase(unittest.TestCase):
    def test_success(self):
        arr = [5, 2, 4, 1, 13, 8]
        quick_sort(arr)
        self.assertEqual(arr, [1, 2, 4, 5, 8, 13])

    def test_repeated_values(self):
        arr = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        quick_sort(arr)
        self.assertEqual(arr, [1, 1, 1, 2, 2, 2, 3, 3, 3])

    def test_single_value(self):
        arr = [1]
        quick_sort(arr)
        self.assertEqual(arr, [1])


class RadixSortTestCase(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(flatten([[1], [2], [3]]), [1, 2, 3])

    def test_get_num_digits(self):
        self.assertEqual(get_num_digits(123456), 6)

    def test_max_digits(self):
        self.assertEqual(get_max_digits([1, 11, 111]), 3)

    def test_get_ith_digit(self):
        self.assertEqual(get_ith_digit(123456, 2), 4)

    def test_success(self):
        self.assertEqual(radix_sort([1, 5, 2, 8, 3, 0, 65]), [0, 1, 2, 3, 5, 8, 65])
        self.assertEqual(
            radix_sort([111, 15, 22242, 84, 3, 0, 65]),
            [
                0,
                3,
                15,
                65,
                84,
                111,
                22242,
            ],
        )

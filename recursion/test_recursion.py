from typing import Callable
import unittest
from recursion import (
    collect_odd_values,
    collect_odd_values_pure,
    power,
    factorial,
    product_of_array,
    sum_range,
    fib,
    reverse,
    is_palindrome,
    some_recursive,
    flatten_pure,
    flatten_helper,
    capitalize_first,
    nested_even_sum,
    capitalize_words,
    stringify_numbers,
    collect_strings,
)


class CollectOddValuesTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(collect_odd_values([1, 2, 3, 4, 5]), [1, 3, 5])


class CollectOddValuesPureTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(collect_odd_values_pure([1, 2, 3, 4, 5]), [1, 3, 5])


class PowerTestCase(unittest.TestCase):
    def test_power_of_zero(self):
        self.assertEqual(power(2, 0), 1)

    def test_success(self):
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(4, 4), 256)


class Factorial(unittest.TestCase):
    def test_success(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(7), 5040)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)


class ProductsOfArrayTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(product_of_array([1, 2, 3]), 6)
        self.assertEqual(product_of_array([1, 2, 3, 10]), 60)

    def test_empty_array_fail(self):
        with self.assertRaises(Exception) as e:
            product_of_array([])
        self.assertEqual(str(e.exception), "cannot pass an empty list")


class SumRangeTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(sum_range(6), 21)
        self.assertEqual(sum_range(10), 55)


class FibTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(28), 317811)
        self.assertEqual(fib(35), 9227465)


class ReverseTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(reverse("abc"), "cba")


class IsPalindromeTestCase(unittest.TestCase):
    def test_success(self):
        self.assertTrue(is_palindrome("tacocat"))
        self.assertTrue(is_palindrome("amanaplanacanalpanama"))

    def test_fail(self):
        self.assertFalse(is_palindrome("awesome"))
        self.assertFalse(is_palindrome("foobar"))
        self.assertFalse(is_palindrome("amanaplanacanalpandemonium"))


class SomeRecursiveTestCase(unittest.TestCase):
    def setUp(self):
        self.is_odd: Callable[[int], bool] = lambda num: num % 2 != 0

    def test_success(self):
        self.assertTrue(some_recursive([1, 2, 3, 4], self.is_odd))
        self.assertTrue(some_recursive([4, 6, 9], self.is_odd))

    def test_fail(self):
        self.assertFalse(some_recursive([4, 6, 8], self.is_odd))
        self.assertFalse(some_recursive([4, 6, 8], lambda val: val > 10))


class FlattenHelperTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(flatten_helper([1, 2, 3, [4, 5]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten_helper([1, [2, [3, 4], [[5]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten_helper([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(flatten_helper([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]), [1, 2, 3])


class FlattenPureTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(flatten_pure([1, 2, 3, [4, 5]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten_pure([1, [2, [3, 4], [[5]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten_pure([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(flatten_pure([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]), [1, 2, 3])


class CapitalizeFirstTestCase(unittest.TestCase):
    def test_success(self):
        self.assertEqual(
            capitalize_first(["car", "taco", "banana"]), ["Car", "Taco", "Banana"]
        )


class NestedEvenSumTestCase(unittest.TestCase):
    def test_success(self):
        dict1 = {
            "outer": 2,
            "obj": {
                "inner": 2,
                "otherObj": {
                    "superInner": 2,
                    "notANumber": True,
                    "alsoNotANumber": "yup",
                },
            },
        }

        dict2 = {
            "a": 2,
            "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
            "c": {"c": {"c": 2}, "cc": "ball", "ccc": 5},
            "d": 1,
            "e": {"e": {"e": 2}, "ee": "car"},
        }

        self.assertEqual(nested_even_sum(dict1), 6)
        self.assertEqual(nested_even_sum(dict2), 10)


class CapitalizeWordsTestCase(unittest.TestCase):
    def test_success(self):
        words = ["i", "am", "learning", "recursion"]
        self.assertEqual(capitalize_words(words), ["I", "AM", "LEARNING", "RECURSION"])


class StringifyNumbersTestCase(unittest.TestCase):
    def test_success(self):
        dict = {
            "num": 1,
            "test": [],
            "data": {
                "val": 4,
                "info": {
                    "isRight": True,
                    "random": 66,
                },
            },
        }

        expected = {
            "num": "1",
            "test": [],
            "data": {
                "val": "4",
                "info": {
                    "isRight": True,
                    "random": "66",
                },
            },
        }

        self.assertEqual(stringify_numbers(dict), expected)


class CollectStringsTestCase(unittest.TestCase):
    def test_success(self):
        dict = {
            "stuff": "foo",
            "data": {
                "val": {
                    "thing": {
                        "info": "bar",
                        "moreInfo": {
                            "evenMoreInfo": {
                                "weMadeIt": "baz",
                            },
                        },
                    },
                },
            },
        }

        self.assertEqual(collect_strings(dict), ["foo", "bar", "baz"])

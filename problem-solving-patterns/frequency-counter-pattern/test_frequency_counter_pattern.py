import unittest
from random import randrange
from frequency_counter_pattern import same, same_naive, is_anagram
from utils.time import time_func


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class SameTestCase(unittest.TestCase):
    def test_success(self):
        arr_1 = [1, 2, 3]
        arr_2 = [4, 1, 9]
        self.assertTrue(same_naive(arr_1, arr_2))
        self.assertTrue(same(arr_1, arr_2))

    def test_number_of_items_fail(self):
        arr_1 = [1, 2, 3]
        arr_2 = [1, 9]
        self.assertFalse(same_naive(arr_1, arr_2))
        self.assertFalse(same(arr_1, arr_2))

    def test_number_frequency_fail(self):
        arr_1 = [1, 2, 1]
        arr_2 = [4, 4, 1]
        self.assertFalse(same_naive(arr_1, arr_2))
        self.assertFalse(same(arr_1, arr_2))

    def test_faster_than_naive(self):
        arr_1 = [randrange(10000) for n in range(10000)]
        arr_2 = [n ** 2 for n in arr_1]
        (delta_naive) = time_func(lambda: same_naive(arr_1, arr_2))
        (delta_frequency_dict) = time_func(lambda: same(arr_1, arr_2))
        self.assertGreater(delta_naive, delta_frequency_dict * 2)


class IsAnagramTestCase(unittest.TestCase):
    def test_success(self):
        self.assertTrue(is_anagram("anagram", "nagaram"))
        self.assertTrue(is_anagram("qwerty", "qeyrwt"))
        self.assertTrue(is_anagram("texttwisttime", "timetwisttext"))

    def test_two_empty_strings(self):
        self.assertTrue(is_anagram("", ""))

    def test_frequency_fail(self):
        self.assertFalse(is_anagram("aaz", "zza"))

    def test_same_length_fail(self):
        self.assertFalse(is_anagram("rat", "car"))

    def test_same_set_different_length_fail(self):
        self.assertFalse(is_anagram("awesome", "awesom"))

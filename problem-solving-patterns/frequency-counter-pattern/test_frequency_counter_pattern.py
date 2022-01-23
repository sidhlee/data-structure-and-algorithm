import unittest
from frequency_counter_pattern import same


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
        self.assertTrue(same(arr_1, arr_2))

    def test_number_of_items_fail(self):
        arr_1 = [1, 2, 3]
        arr_2 = [1, 9]
        self.assertFalse(same(arr_1, arr_2))

    def test_number_frequency_fail(self):
        arr_1 = [1, 2, 1]
        arr_2 = [4, 4, 1]
        self.assertFalse(same(arr_1, arr_2))

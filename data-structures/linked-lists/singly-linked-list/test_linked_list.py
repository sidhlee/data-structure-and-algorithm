import unittest
from linked_list import SinglyLinkedList


class SinglyLinkedListTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = SinglyLinkedList()

    def test_properties(self):
        self.assertEqual(self.sut.length, 0)
        self.assertEqual(self.sut.head, None)
        self.assertEqual(self.sut.tail, None)

    def test_push(self):
        self.sut.push(1)
        self.sut.push(2)
        self.assertEqual(self.sut.length, 2)
        self.assertEqual(self.sut.head.value, 1)
        self.assertEqual(self.sut.head.next.value, 2)
        self.assertEqual(self.sut.tail.value, 2)

    def test_pop_empty_list(self):
        val = self.sut.pop()
        self.assertEqual(val, None)
        self.assertEqual(self.sut.head, None)
        self.assertEqual(self.sut.tail, None)

    def test_pop_only_item(self):
        self.sut.push(1)
        val = self.sut.pop()
        self.assertEqual(val, 1)
        self.assertEqual(self.sut.head, None)
        self.assertEqual(self.sut.tail, None)

    def test_pop_multiple_item(self):
        self.sut.push(1)
        self.sut.push(2)
        val = self.sut.pop()
        self.assertEqual(val, 2)
        self.assertEqual(self.sut.head.value, 1)
        self.assertEqual(self.sut.tail.value, 1)

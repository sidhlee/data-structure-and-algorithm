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

    def test_push_chainable(self):
        self.sut.push(1).push(2)
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

    def test_pop_multiple_items(self):
        self.sut.push(1)
        self.sut.push(2)
        val = self.sut.pop()
        self.assertEqual(val, 2)
        self.assertEqual(self.sut.head.value, 1)
        self.assertEqual(self.sut.tail.value, 1)

    def test_unshift(self):
        self.sut.unshift(1).unshift(2)
        self.assertEqual(self.sut.length, 2)
        self.assertEqual(self.sut.head.value, 2)
        self.assertEqual(self.sut.head.next.value, 1)
        self.assertEqual(self.sut.tail.value, 1)

    def test_shift_empty_list(self):
        val = self.sut.shift()
        self.assertEqual(val, None)
        self.assertEqual(self.sut.head, None)
        self.assertEqual(self.sut.tail, None)

    def test_shift_single_item(self):
        self.sut.unshift(1)
        val = self.sut.shift()
        self.assertEqual(val, 1)
        self.assertEqual(self.sut.length, 0)
        self.assertEqual(self.sut.head, None)
        self.assertEqual(self.sut.tail, None)

    def test_shift_multiple_items(self):
        self.sut.unshift(1).unshift(2)
        val = self.sut.shift()
        self.assertEqual(val, 2)
        self.assertEqual(self.sut.length, 1)
        self.assertEqual(self.sut.head.value, 1)
        self.assertEqual(self.sut.tail.value, 1)

    def test_get_node_success(self):
        self.sut.push(1).push(2).push(3)
        node = self.sut.get_node(1)
        self.assertEqual(node, self.sut.head.next)

    def test_get_empty_list(self):
        with self.assertRaises(IndexError):
            self.sut.get(0)

    def test_get_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.sut.push(1)
            self.sut.get(1)

    def test_get_single_item(self):
        self.sut.push(1)
        value = self.sut.get(0)
        self.assertEqual(value, 1)
        self.assertEqual(self.sut.head.value, 1)
        self.assertEqual(self.sut.tail.value, 1)
        self.assertEqual(self.sut.length, 1)

    def test_get_multiple_items(self):
        self.sut.push(1).push(2).push(3).push(4).push(5)
        value = self.sut.get(3)
        self.assertEqual(value, 4)
        self.assertEqual(self.sut.length, 5)

    def test_set_empty_list(self):
        with self.assertRaises(IndexError):
            self.sut.set(777, 0)

    def test_set_index_out_of_range(self):
        self.sut.push(1)
        with self.assertRaises(IndexError):
            self.sut.set(777, 1)

    def test_set_success(self):
        self.sut.push(1).push(2).push(3)
        self.sut.set("two", 1).set("three", 2)
        self.assertEqual(self.sut.head.next.value, "two")
        self.assertEqual(self.sut.tail.value, "three")

    def test_insert(self):
        self.sut.insert("first", 0).insert("third", 1).insert("second", 1)
        self.assertEqual(self.sut.head.value, "first")
        self.assertEqual(self.sut.head.next.value, "second")
        self.assertEqual(self.sut.tail.value, "third")
        self.assertEqual(self.sut.length, 3)

    def test_insert_empty_list(self):
        self.sut.insert("first", 0)
        self.assertEqual(self.sut.head.value, "first")
        self.assertEqual(self.sut.tail.value, "first")
        self.assertEqual(self.sut.length, 1)

    def test_insert_at_tail(self):
        self.sut.insert("first", 0).insert("second", 1).insert("third", 2)
        self.assertEqual(self.sut.head.value, "first")
        self.assertEqual(self.sut.head.next.value, "second")
        self.assertEqual(self.sut.tail.value, "third")
        self.assertEqual(self.sut.length, 3)

    def test_insert_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.sut.insert("first", 1)

    def test_remove_success(self):
        self.sut.push(0).push(1).push(2)
        removed_value = self.sut.remove(1)
        self.assertEqual(removed_value, 1)
        self.assertEqual(self.sut.head.next, self.sut.tail)
        self.assertEqual(self.sut.length, 2)

    def test_remove_empty_list(self):
        with self.assertRaises(IndexError):
            self.sut.remove(0)

    def test_remove_out_of_range(self):
        self.sut.push(0).push(1).push(2)
        with self.assertRaises(IndexError):
            self.sut.remove(3)

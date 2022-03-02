import unittest
from node import Node


class NodeTestCase(unittest.TestCase):
    def test_properties(self):
        node = Node(1)
        self.assertEqual(node.value, 1)
        self.assertEqual(node.next, None)

    def test_can_link(self):
        first = Node(1)
        second = Node(2)
        third = Node(3)
        first.next = second
        second.next = third
        self.assertEqual(first.next.next, third)

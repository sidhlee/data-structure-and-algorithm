from unittest import TestCase
from challenges.trees.tree_constructor import tree_constructor


class TreeConstructorTests(TestCase):
    def test__true(self):
        self.assertEqual(
            tree_constructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]), "true"
        )

    def test__true__double_digit(self):
        self.assertEqual(
            tree_constructor(["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)"]),
            "true",
        )

    def test__false(self):
        self.assertEqual(
            tree_constructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]), "false"
        )

    def test__false__two_parents(self):
        self.assertEqual(tree_constructor(["(2,5)", "(2,6)"]), "false")

    def test__false__disconnected(self):
        self.assertEqual(tree_constructor(["(9,8)", "(6,5)"]), "false")

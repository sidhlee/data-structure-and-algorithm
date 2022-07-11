from typing import Optional

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
'./validate_binary_search_tree_1.jpeg'

Input: root = [2,1,3]
Output: true
Example 2:
'./validate_binary_search_tree_2.jpeg'

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST_minmax(self, root: Optional[TreeNode]) -> bool:
        """
        Runtime: 76 ms (88%)
        Memory Usage: 16.6 MB (45%)
        pass minmax when calling helper recursively with left or right child.
        minmax value is updated in relation to the current value and the position of the children.
        eg. when calling with left child, max value would be the current node value and the min value
        the most recently updated min value from the ancestors.

        The range gets narrower as traversing down on a binary tree
        """

        def inner(root, min=float("-inf"), max=float("inf")):
            if root is None:
                return True
            if root.val <= min or root.val >= max:
                return False
            return inner(root.left, min, root.val) and inner(root.right, root.val, max)

        return inner(root)

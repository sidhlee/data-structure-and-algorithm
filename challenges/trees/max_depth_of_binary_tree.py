from typing import Optional

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Example 1:
'./max_depth_of_binary_tree_1.jpeg'

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

Hint1
- you need to consider perfectly unbalanced tree where there are only left/right children.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth_recursion(self, root: Optional[TreeNode]) -> int:
        """
        2022-07-07 07:57:09
        Runtime: 68 ms (41%)
        Memory Usage: 16.3 MB (55%)

        Recursively call with left and right child.
        Return 0 when reaching the null.
        From one level up, take the larger value of the left and right children
        and add 1 for itself (this also applies to the leaf node).

        TODO: try dfs approach where you pass the child node and the incrementing level to the inner helper
        and when reaching the leaf, update the result property if the level is greater than the current result.
        -> In OPP, you don't need nonlocal! just use class field

        """
        # covers when the initial input is None
        if root is None:
            return 0
        # we don't need this since we're doing + 1
        # if root.left is None and root.right is None:
        #     return 1
        return (
            max(self.maxDepth_recursion(root.left), self.maxDepth_recursion(root.right))
            + 1
        )

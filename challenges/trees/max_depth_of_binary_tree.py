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

        This method use DFS and increments max_depth during the backtracking.
        It always takes the max between left and right -> last step would be on the root node
        When current node is None we return 0 -> if both left and right are None, the parent is a leaf node -> start adding 1 to the depth and keep backtracking

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

    def maxDepth_iterative_dynamic(self, root: Optional[TreeNode]) -> int:
        '''
        2022-09-03 09:21:25
        Runtime: 37 ms (99%)
        Memory Usage: 15.3 MB (81%)

        Finding max -> we don't care about the order -> can use stack instead of queue
        Push left and right and update max as we go only if curr_node is not None

        Edge cases covered:
        - When there's zero node in the tree, max_depth stays 0
        - When curr_node is the leaf node, we're appending None for left and right
        - but we're only updating max_depth only when the curr_node is not None
        '''
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            curr_node, curr_depth = stack.pop()
            if curr_node:
                stack.append((curr_node.left, curr_depth + 1))
                stack.append((curr_node.right, curr_depth + 1))
                max_depth = max(max_depth, curr_depth) # leaf node would have null for both left and right
        return max_depth

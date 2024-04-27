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
    def maxDepth_recursion_bubble_up(self, root: Optional[TreeNode]) -> int:
        """
        2022-12-01 09:00:24
        Creates inner function to count the depth on the way down and bubble up the max_depth when it reaches the leaf node
        """

        def inner(node, curr_depth):
            if not node:
                return curr_depth - 1
            return max(
                inner(node.left, curr_depth + 1), inner(node.right, curr_depth + 1)
            )

        return inner(root, 1)

    def maxDepth_recursion_compute_way_down(self, root: Optional[TreeNode]) -> int:
        """
        2024-04-27 13:49:19

        Logic more readable than the previous one.
        More intuitive than computing on the way up.
        """

        def traverse(node, curr_depth):
            if not node:
                return curr_depth
            # If the current node exists, count the depth and go down to the next level
            curr_depth += 1
            return max(
                traverse(node.left, curr_depth), traverse(node.right, curr_depth)
            )

        # We don't know if the root exists or not, so start with curr_depth = 0
        return traverse(root, 0)

    def maxDepth_recursion_compute_way_up(self, root: Optional[TreeNode]) -> int:
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

        2022-12-01 09:02:32
        This approach computes the depth on the way up by adding 1 to the return value at each level.
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
        """
        2022-09-03 09:21:25
        Runtime: 37 ms (99%)
        Memory Usage: 15.3 MB (81%)

        Finding max -> we don't care about the order -> can use stack instead of queue
        Push left and right and update max as we go only if curr_node is not None

        Edge cases covered:
        - When there's zero node in the tree, max_depth stays 0
        - When curr_node is the leaf node, we're appending None for left and right
        - but we're only updating max_depth only when the curr_node is not None
        """
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            curr_node, curr_depth = stack.pop()
            if curr_node:
                stack.append((curr_node.left, curr_depth + 1))
                stack.append((curr_node.right, curr_depth + 1))
                max_depth = max(
                    max_depth, curr_depth
                )  # leaf node would have null for both left and right
        return max_depth

    def maxDepth_stack_dynamic_better(self, root: Optional[TreeNode]) -> int:
        """
        2022-10-26 08:10:30
        Runtime: 48 ms (87%)
        Memory Usage: 15.3 MB (90%)

        This still uses O(n) space but less than a recursion which stores entire stack frame.
        By checking the child node, we don't append the null node and this will save
        maximum max_depth ^ 2 number of iterations.
        """
        max_depth = 0
        stack = [(root, 1)]
        while stack and stack[0][0]:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth

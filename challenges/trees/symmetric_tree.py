from typing import Optional
from collections import deque


"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
'./symmetric_tree_1.jpeg'

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:
'./symmetric_tree_2.jpeg'

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric_bfs(self, root: Optional[TreeNode]) -> bool:
        """
        2022-07-11 08:03:48
        Runtime: 38 ms (87%)
        Memory Usage:14 MB (60%)

        Using BFS to get all nodes on the same level and check symmetry
        This algo checks from the root node and returns as soon as finding non-symmetric level.
        """

        def check(nodes):
            mid = len(nodes) // 2
            vals = [x.val if x is not None else None for x in nodes]
            return vals[mid - 1 :: -1] == vals[mid:]

        queue = deque([root])
        while queue:
            nodes = []
            # num nodes is capped at 1000 so nested loop is ok
            while queue:
                # empty the queue and get all the nodes at the current level
                curr = queue.popleft()
                # not sure why it works even though nodes is missing the children of null node.
                if curr is None:
                    continue
                nodes.append(curr.left)
                nodes.append(curr.right)
            # get out if current level is empty
            if not ([x for x in nodes if x is not None]):
                return True
            # check symmetry if current level is not empty
            if not check(nodes):
                return False
            # set the checked nodes as the new queue
            queue = deque(nodes)

    def isSymmetric_recursion_optimized(self, root: Optional[TreeNode]) -> bool:
        """
        2022-07-13 07:07:41
        Runtime: 39 ms (85%)
        Memory Usage: 13.8 MB (94%)

        Using recursion to traverse to the outermost leaves then backup to traverse to the inner nodes.

        base case:
        - both children are None

        not symmetric if:
        - only one of the nodes is None
        - if node values are not equal

        optimization:
        This algorithm checks the entire tree and start again with the first left and right child switched.
        will return True if the passed nodes are right and left child of the root.
        """

        def is_sym(node1, node2):
            if node1 is root.right and node2 is root.left:
                return True
            if node1 is None and node2 is None:
                return True
            if (node1 is None) != (node2 is None):
                return False
            if node1.val != node2.val:
                return False

            return is_sym(node1.left, node2.right) and is_sym(node1.right, node2.left)

        return is_sym(root, root)

    def isSymmetric_recursion_skip_root_node(self, root: Optional[TreeNode]) -> bool:
        """
        2022-09-07 07:37:02
        Runtime: 47 ms (67%)
        Memory Usage: 14 MB (61%)

        Take advantage of assumption: length >= 1 and start at level 1 instead of root node.
        Now we don't need extra check from the inner function.

        Optimization idea:
        - Now we're calling inner 2 more times to check for the leaf node passing outer children and inner children.
        - We can check whether nth_left and nth_right are both leaf nodes then return nth_left.val == nth_right.val inside inner function.
        - Avoiding/catching AttributeError might be tricky.
        """

        def inner(nth_left, nth_right):
            if nth_left is None and nth_right is None:
                return True
            elif nth_left is None or nth_right is None:
                return False
            elif nth_left.val != nth_right.val:
                return False
            return inner(nth_left.left, nth_right.right) and inner(
                nth_left.right, nth_right.left
            )

        return inner(root.left, root.right)

    def isSymmetric_recursion_better_condition(self, root: Optional[TreeNode]) -> bool:
        """
        2022-12-02 09:05:15
        condition more readable
        """

        def inner(left_node, right_node):
            if left_node is None and right_node is None:
                return True
            elif left_node and right_node and left_node.val == right_node.val:
                return inner(left_node.left, right_node.right) and inner(
                    left_node.right, right_node.left
                )
            return False

        return inner(root.left, root.right)

    def isSymmetric_either_none_but_not_both(self, root: Optional[TreeNode]) -> bool:
        """
        2024-02-27 06:01:35

        simplify condition for checking if either of the nodes is None but not both
        """

        def inner(left, right):
            if not left or not right:
                return left is right
            if left.val != right.val:
                return False
            return inner(left.left, right.right) and inner(left.right, right.left)

        return inner(root.left, root.right)

    def isSymmetric_stack_in_pair(self, root: Optional[TreeNode]) -> bool:
        """
        2024-02-27 06:16:11

        Uses stack instead of queue because the order doesn't matter.
        1. init stack with left and right node from root
        2. while stack is not empty, pop two nodes from the stack
        3. if both nodes are None, ignore and continue
        4. if only one of nodes is None or the values are different, return False
        5. append the mirroring pairs to the stack
        6. if stack is empty -> checked all nodes from the tree -> return True
        """

        stack = [root.left, root.right]
        while stack:
            one, two = stack.pop(), stack.pop()
            if not one and not two:
                continue
            if (not one or not two) or one.val != two.val:
                return False
            stack += [one.left, two.right, one.right, two.left]
        return True

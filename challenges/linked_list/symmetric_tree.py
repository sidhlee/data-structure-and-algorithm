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

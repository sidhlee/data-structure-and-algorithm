from typing import Optional, List
from collections import deque

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
'./level_order_1.jpeg'

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: [] 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Runtime: 32 ms (97%)
        Memory Usage: 14.2 MB (84%)

        Use BFS to create a list of sibling nodes inside inner loop
        and append the list to the result in outer loop
        """
        if root is None:
            return None
        queue = deque([root])
        result = [[root.val]]
        while queue:
            nodes = []
            while queue:
                node = queue.popleft()
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if nodes:
                result.append([x.val for x in nodes if x is not None])
                queue = deque(nodes)
        return result

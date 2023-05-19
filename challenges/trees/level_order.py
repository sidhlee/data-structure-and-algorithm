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

    def levelOrder_linear(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        2022-09-11 19:23:54
        Runtime: 42 ms (82%)
        Memory Usage: 14.2 MB (53%)

        append to the temp list with BFS with the level of the node,
        then construct the result by looping through the temp list.
        """
        if not root:
            return []
        queue = deque([(root, 0)])
        nodes = []
        result = []
        while queue:
            node, level = queue.popleft()
            nodes.append((node, level))
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        for node, level in nodes:
            if level >= len(result):
                result.append([])
            result[level].append(node.val)
        return result

    def levelOrder_recursion(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Runtime: 48 ms (68%)
        Memory Usage: 14.9 MB (10%)

        recursion version of the above.
        NOT memory efficient, but more readable (have to keep all call stack frames)
        """
        result = []

        def inner(node, level=0):
            if not node:
                return
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            inner(node.left, level + 1)
            inner(node.right, level + 1)

        inner(root)
        return result

    def levelOrder_linear_optimized(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Runtime: 38 ms (90%)
        Memory Usage: 14.2 MB (85%)

        queue nodes with their levels
        Use BFS to enqueue child nodes with level incremented from the dequeued node,
        and append the value of dequeued node to the result array at the matching index which should be same as the node level.
        we check for the dequeued node, so an empty root node would not append anything to the result.
        """
        queue = deque([(root, 0)])
        result = []
        while queue:
            node, level = queue.popleft()
            if node:
                if level == len(result):
                    result.append([])
                result[level].append(node.val)
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        return result

    def levelOrder_check_before_loop(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        2022-10-27 08:14:13

        queue should be empty if there's no node -> easier to read
        """
        res = []
        queue = deque([(root, 0)]) if root else None
        while queue:
            node, level = queue.popleft()
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return res

    def levelOrder_check_with_queue(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        2023-05-19 08:34:28
        Don't get into the loop if given root is empty
        """
        res = []
        queue = deque([(root, 0)])
        while queue and root:
            node, level = queue.popleft()
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return res

from typing import List, Optional

"""
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node
never differs by more than one.

Example 1:
'./sorted_array_to_bst_1.jpeg'

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
'./sorted_array_to_bst_2.jpeg'

Example 2:
'./sorted_array_to_bst_3.jpeg'

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST_recursion(self, nums: List[int]) -> Optional[TreeNode]:
        """
        2022-07-14 08:38:00
        Runtime: 119 ms (64%)
        Memory Usage: 15.6 MB (83%)

        Keep finding middle node from the subarray and attach it to the parent as left or right child.
        Call itself twice with the middle node as parent and the left and right subarray.
        """
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        if len(nums) == 1:
            return root

        def inner(node, arr):
            if not arr:
                return
            mid = len(arr) // 2
            mid_node = TreeNode(arr[mid])
            left = arr[:mid]
            right = arr[mid + 1 :]
            if mid_node.val < node.val:
                node.left = mid_node
            else:
                node.right = mid_node
            if left:
                inner(mid_node, left)
            if right:
                inner(mid_node, right)

        inner(root, nums[:mid])
        inner(root, nums[mid + 1 :])

        return root

    def sortedArrayToBST_set_recursively(self, nums: List[int]) -> Optional[TreeNode]:
        """
        2022-07-14 08:38:02
        Runtime: 67 ms (90%)
        Memory Usage: 15.6 MB (83%)

        Instead of passing current node and array to conditionally attach the mid,
        only pass the array to find the middle node and set left and right recursively.

        * The middle of the left and right sub-array will always be the middle value within the subarray
            when the array is sorted.
        """

        def inner(arr):
            if not arr:
                return
            mid = len(arr) // 2
            mid_node = TreeNode(arr[mid])
            mid_node.left = inner(arr[:mid])
            mid_node.right = inner(arr[mid + 1 :])
            return mid_node

        return inner(nums)

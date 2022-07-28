"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
'./merge_two_sorted_lists_1.jpeg'

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists_two_pointers(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        2022-07-02 17:24:52
        Runtime: 42 ms (85%)
        Memory Usage: 13.9 MB (79%)

        Using one pointer to traverse, and the other to keep track of the other list.
        Feel like I was lucky to come up with this. Practice more!

        Try the solution that doesn't mutate the original lists
        """
        # to return early if one or both lists are empty.
        if not list1 or not list2:
            return list1 if not list2 else list2

        # set the list with the smaller first node as the head
        head = list1 if list1.val < list2.val else list2
        curr = head
        other = list2 if list1.val < list2.val else list1

        # stop if curr or other becomes None
        while curr and other:
            # If curr is the last node, connect it to the other pointer
            if curr.next is None or other.val < curr.next.val:
                temp = curr.next
                # After setting the other as the next, move the curr to it
                curr.next = other
                curr = other
                # set the old next as the other
                other = temp
            # if curr is not the last node and other pointer's value is greater than current node's next
            else:
                curr = curr.next
        # If other or curr reached the end, we just leave it as it is
        # this covers the following 2 cases:
        # 1. other points at None and there are more nodes following curr -> all good
        # 2. curr reached the end and other has more nodes -> we still get into the if block and and connect curr to other
        return head

    def mergeTwoLists_pure(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        2022-07-05 06:55:16
        Runtime: 54 ms (57%)
        Memory Usage: 13.8 MB (79%)

        Does not mutate the input lists and returns a new merged head.
        """
        if not list1 or not list2:
            return list1 if not list2 else list2
        curr1, curr2 = (list1, list2) if list1.val < list2.val else (list2, list1)
        merged = ListNode(curr1.val)
        curr_merged = merged
        curr1 = curr1.next
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr_merged.next = curr1
                curr1 = curr1.next
            else:
                curr_merged.next = curr2
                curr2 = curr2.next
            curr_merged = curr_merged.next
        # connect the remaining nodes
        curr_merged.next = curr1 if curr1 else curr2
        return merged

    def mergeTwoLists_recursion(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        2022-07-06 07:22:38
        Runtime: 41 ms (87%)
        Memory Usage: 13.8 MB (79%)

        Using recursion - diminishing input strategy
        - connect to the smaller node recursively passing next of the smaller node
        - For base case, return other list when one of the list passed is None
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists_recursion(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_recursion(list1, list2.next)
            return list2

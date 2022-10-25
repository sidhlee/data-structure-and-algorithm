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

    def mergeTwoLists_recursion_pure(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        2022-10-24 18:55:03
        """

        def chain_next(node1, node2):
            if not node1 or not node2:
                return node2 if not node1 else node1
            if node1.val < node2.val:
                node1.next = chain_next(node1.next, node2)
                return node1
            else:
                node2.next = chain_next(node1, node2.next)
                return node2

        head = ListNode()
        head.next = chain_next(list1, list2)
        return head.next

    def mergeTwoLists_start_with_empty_node(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        2022-08-30 18:53:04
        Runtime: 36 ms (96%)
        Memory Usage: 13.8 MB (79%)

        No need to do the same comparison before getting into the loop.
        Start with an empty node and keep chaining after it.
        We can return what's next to the empty head.
        """
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        return head.next

    def mergeTwoLists_return_next_pure(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        2022-10-24 17:42:13
        Does not mutate the input lists.
        If you create an empty node as the head and return the next,
        it also handles the case where one or both of them are None because
        next node is initialized as None.
        After getting out of the loop because one of both of pointers are empty,
        we're attaching the first pointer if it's not empty.
        This takes care of all the following cases:
        - p1 not None, p2 None
        - p2 not None, p1 None
        - p1 None, p2 None
        """
        curr1, curr2 = list1, list2
        curr = head = ListNode()
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        curr.next = curr1 if curr1 else curr2
        return head.next

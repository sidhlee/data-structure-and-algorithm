"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
'./reverse_linked_list_1.jpeg'

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
'./reverse_linked_list_2.jpeg'

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_n_square(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        2022-07-01T15:07:15.016Z
        Naive iterative solution.

        This one didn't pass the time limit for [5000 - x for x in range(5000)]
        """
        if not head:
            return

        def swap(n1, n2):
            temp = n1.val
            n1.val = n2.val
            n2.val = temp

        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        left = head
        for i in range(length // 2):
            right = head
            for j in range(length - i - 1):
                right = right.next
            print(left.val, right.val)
            swap(left, right)
            print(head)
            left = left.next

        return head

    def reverseList_list_index(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        2022-07-01T15:07:19.031Z
        Runtime: 59 ms (40%)
        Memory Usage: 15.4 MB (56%)

        Store node references to a list and swap values using index.
        """
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        for left in range(len(nodes) // 2):
            right = len(nodes) - 1 - left
            nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val

        return head

    def reverseList_changing_directions(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        2022-07-01 11:50:34
        Runtime: 36 ms (94%)
        Memory Usage: 15.4 MB (56%)

        Only reversing the next using 3 pointers:
        - temp: used to store original next
        - curr: to traverse through
        - prev: to point next to

        Don't worry about temporarily broken link after making next to point to prev.
        We stored the reference to the next before changing direction.
        """
        prev = None
        curr = head
        while curr:
            temp = curr.next  # save next before changing it
            curr.next = prev  # point next to prev
            prev = curr  # move prev to curr
            curr = temp  # move curr to saved next
        return prev

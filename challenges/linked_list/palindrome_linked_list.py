"""
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
'./palindrome_linked_list_1.jpeg'

Input: head = [1,2,2,1]
Output: true
Example 2:
'./palindrome_linked_list_2.jpeg'

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome_reverse_and_compare(self, head: Optional[ListNode]) -> bool:
        """
        2022-07-02 18:32:29
        Runtime: 718 ms (99%)
        Memory Usage: 31.3 MB (93%)

        Using the previous reversing algorithm, reverse the fist half then compare nodes with the ones in the second half
        """
        # get the length of the list in order to find the middle
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        right = head
        prev = None
        # reverse the first half
        for _ in range(n // 2):
            temp = right.next
            right.next = prev
            prev = right
            right = temp
        head = prev
        # move over the right from the dead center.
        right = right.next if n % 2 == 1 else right
        while right and head:
            if head.val != right.val:
                return False
            head = head.next
            right = right.next
        return True

    def isPalindrome_reverse_while_finding_middle(
        self, head: Optional[ListNode]
    ) -> bool:
        """
        2022-08-31 16:42:42
        Runtime: 770 ms (97%)
        Memory Usage: 31.1 MB (98%)

        Instead of looping twice for finding the list size and reversing up to the middle,
        we use the second index counter to reverse the first half of where the right pointer is in each iteration.
        """
        right = left = head
        i = j = 0
        prev = None
        while right:
            if j < i / 2:
                j += 1
                temp = left.next
                left.next = prev
                prev = left
                left = temp
            right = right.next
            i += 1
        if i % 2 != 0:
            left = left.next
        while left and prev:
            if left.val != prev.val:
                return False
            left, prev = left.next, prev.next
        return True

    def isPalindrome_reverse_first_half_one_index(
        self, head: Optional[ListNode]
    ) -> bool:
        """
        2022-10-25 07:10:17

        We can move left every second time to find middle
        - left is right / 2 when there are even number of nodes
        - left is right / 2 - 1 when there are odd number of nodes
        eg.
        i = 0 1 2 3 4
        R = 0 1 2 3 4
        L = 0 0 1 1 2
        """
        # find middle
        i = 0
        left = right = head
        prev = None
        while right:
            right = right.next
            if i % 2 == 1:
                temp = left.next
                left.next = prev
                prev = left
                left = temp
            i += 1
        # move left to the right of the middle when there are odd number of nodes
        if i % 2 == 1:
            left = left.next
        # if prev is None, there is one or no node in the list
        while left and prev:
            if left.val != prev.val:
                return False
            prev = prev.next
            left = left.next
        return True

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

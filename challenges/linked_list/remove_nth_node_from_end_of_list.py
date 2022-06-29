"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:
'./remove_nth_node_from_end_of_list_01.jpeg'

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

Hint1: 
Maintain two pointers and update one with a delay of n steps.

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd_follow_behind(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        2022-06-29T11:57:03.359Z
        Runtime: 35 ms (90%)
        Memory Usage: 13.9 MB (69%)

        Using 3 pointers + 1 counter:
        - i: counter to move left and pre behind right
        - right: to iterate through the list and find nth by stopping once out of range
        - left: pointing at the nth Node behind right
        - pre: pointing at the previous Node of the left

        Edge cases to consider:
        - when n == size(List), pre stays None and left still points to head
            -> make the head point to the next
        - If the left points a node after head, modify pre.next to skip the left

        * initializing variables in one line reduces runtime/space greatly.
        """
        i, pre, left, right = 0, None, head, head
        while right:
            if i >= n:
                pre = left
                left = left.next
            i += 1
            right = right.next
        if left == head:
            head = head.next
        else:
            pre.next = pre.next.next
        return head

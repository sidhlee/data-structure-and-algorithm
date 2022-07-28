from typing import Optional

"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
'./linked_list_cycle_1.png'

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:
'./linked_list_cycle_2.png'

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:
'./linked_list_cycle_3.png'

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


"""
10^4 is not too bad for n^2
solve it using O(1) space

- we have to use reference to compare
- we have the reference to head
- count the length from head and use that to determine
keep prev
iterate until 
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle_set(self, head: Optional[ListNode]) -> bool:
        """
        2022-07-04 10:04:14
        Runtime: 104 ms (22%)
        Memory Usage: 18 MB (0%)

        Storing all nodes until we find the repeated one.
        Uses linear space.
        """
        s = set()
        curr = head
        while curr:
            if curr in s:
                return True
            s.add(curr)
            curr = curr.next
        return False

    def hasCycle_slow_and_fast(self, head: Optional[ListNode]) -> bool:
        """
        2022-07-04 10:26:37
        Runtime: 100 ms (26%)
        Memory Usage: 17.5 MB (93%)

        Have faster pointer moving 2x as fast.
        If fast meets slow, there's a cycle.
        Checking fast.next to avoid exception
        """
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle_return_faster(self, head: Optional[ListNode]) -> bool:
        """
        2022-07-04 10:50:43
        Runtime: 55 ms (95%)
        Memory Usage: 17.6 MB (66%)

        Returns False for empty head before initializing variables.
        Don't need to set slow and fast to the same variable.
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def hasCycle_try_catch(self, head: Optional[ListNode]) -> bool:
        """
        2022-07-06 08:05:33
        Runtime: 82 ms (53%)
        Memory Usage: 17.5 MB (66%)

        Theoretically this should be faster since we don't check in between iteration,
        but leet code runtime is flaky
        """
        if head is None:
            return False
        slow, fast = head, head.next
        while slow != fast:
            try:
                slow, fast = slow.next, fast.next.next
            except AttributeError:
                return False
        return True

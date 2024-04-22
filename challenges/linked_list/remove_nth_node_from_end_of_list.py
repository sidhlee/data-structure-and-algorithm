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

    def removeNthFromEnd_follow_n_steps_behind(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        2022-11-26 13:25:19
        Variable names are easier to understand
        """
        i = 0
        target = curr = head
        prev = None
        while curr:
            curr = curr.next
            if i >= n:
                prev = target
                target = target.next
            i += 1
        if target == head:
            head = head.next
        else:
            prev.next = target.next
        return head

    def removeNthFromEnd_follow_behind_easier(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        2022-10-20 08:37:51
        Keep track of previous node to the target.
        Initializing pre_target node as None is easier to reason about
        """
        pre_target = None
        curr = head
        i = 0
        while curr:
            curr = curr.next
            if i >= n:
                pre_target = pre_target.next if pre_target else head
            i += 1
        if pre_target:
            pre_target.next = pre_target.next.next
        else:
            head = head.next
        return head

    def removeNthFromEnd_no_next_next(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        2022-07-05 07:54:01
        Runtime: 37 ms (86%)
        Memory Usage: 13.9 MB (69%)

        Comparing a variable to a scalar value is easier to reason about than comparing to another variable.
        Because we're returning head, we have to make the head to point to its next when we want to remove it.
        """
        i, prev = 0, None
        left = right = head
        while right:
            if i >= n:
                prev = left
                left = left.next
            i += 1
            right = right.next
        # removing non-head
        if prev:
            prev.next = left.next
        else:
            # removing head
            head = left.next
        return head

    def removeNthFromEnd__loop_twice(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        2022-08-29 21:37:36
        Runtime: 51 ms (54%)
        Memory Usage: 14 MB (0%)

        loop through once to get the size of the list, then loop once more to access the removing node and prev node.
        -> we could just follow n-steps behind the pointer to access removing node and prev node in the first loop!

        2022-10-20 08:08:25
        However, if we have prev_node, we don't need curr_node to remove target.
        We can simply set the prev_node to the next of target, which includes the case when the target is the last node.

        Conditions within loops can usually be taken out of the loop
        """
        if not head.next and n == 1:
            return None
        sz = 0
        curr_node = head
        while curr_node:
            sz += 1
            curr_node = curr_node.next
        curr_node = head
        prev_node = None
        for i in range(sz):
            # i: 0 1 2 [3] 4
            # p: 0 1 2
            # c: 1 2 3
            # when curr_node is the target
            if i == sz - n:
                # if not the last node, set the curr_node to the next node
                if curr_node.next:
                    curr_node.val = curr_node.next.val
                    curr_node.next = curr_node.next.next
                else:
                    # if last node, remove by setting prev node
                    prev_node.next = None
                return head
            prev_node = curr_node
            curr_node = curr_node.next

    def removeNthFromEnd_2n_simpler(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        2022-10-20 07:55:07

        We can assume that we're removing at least one node,
        so we can have separate logic for removing the first node.
        - set head to the second node and return

        If we're not removing the first node then there must be more than 2 nodes in the list.
        Loop to access the prev node of the target
        and set the prev node's next to the next of the target.
        - This includes the case when the target is the last node.
        -> prev.next = None
        """
        # Find the list length
        sz = 0
        curr = head
        while curr:
            curr = curr.next
            sz += 1

        # Removing the first node. This includes removing only node.
        if sz == n:
            head = head.next
            return head

        # Get prev node and remove target
        prev = head
        for i in range(sz - n - 1):
            prev = prev.next
        prev.next = prev.next.next

        return head

    def removeNthFromEnd_loop_once_easier(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        2022-12-30 10:50:15
        """
        # naming target node as curr is easier to understand because it's the one after the prev node
        prev, curr, right = None, head, head
        # named probing node as right rather than curr because we're only using it to advance the prev and curr.
        while right:
            right = right.next
            # if curr is n behind the right node, we start advancing the curr and prev
            if n <= 0:
                prev = curr
                curr = curr.next
            n -= 1
        # if curr is not the head node, we use prev to remove curr
        if prev:
            prev.next = curr.next
            return head
        # if prev is None (= curr is at head), we return head.next to remove curr
        else:
            return head.next

    def removeNthFromEnd_bad_but_works(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        2023-03-29 08:42:59
        - naming probing cursor as curr -> confusing
        - not having pointer to the removing node -> hard to visualize
        - using extra variable for counting -> use passed n
        - many conditions based on the counter

        Create pointers that represents objects in visualization
        """
        curr = head
        prev_to_removing_node = None
        i = 0

        while curr:
            curr = curr.next
            i += 1
            if i == n + 1:
                prev_to_removing_node = head
            elif i > n + 1:
                prev_to_removing_node = prev_to_removing_node.next
        # here, i is the number of nodes in the list
        if i == 1:
            # only one node in the list. remove it.
            return None
        elif i == 2 and n == 1:
            # two nodes and removing tail. prev node would still be none.
            head.next = None
            return head
        elif i == n:
            # i >= 3 and removing the head
            return head.next
        # i >= 3 and using prev to remove target
        prev_to_removing_node.next = prev_to_removing_node.next.next

        return head

    def removeNthFromEnd_two_pointers(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
         2024-02-20 05:42:46
         Runtime: 27 ms (98%)
         Memory Usage: 16.4 MB (99.8%)

         Uses one less pointer: prev and probe

                            ---->
         Input: head = [1,2,3,4,5], n = 2
                            c   p
                        p
                     c
         Output: [1,2,3,5]

         [1] n = 1, n <= len(nodes)
        c   p
         [1, 2] n = 2
             p  n = 1
               p n = 0
        c
        """
        probe = head
        prev = None
        while probe:
            probe = probe.next
            if n > 0:
                n -= 1
            else:
                prev = head if not prev else prev.next

        # when sz = 1, n = 1 and prev is None
        if prev:
            prev.next = prev.next.next
        # prev is None when removing the head
        return head if prev else head.next

    def removeNthFromEnd_two_pointers_easier(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        2024-04-22 05:44:20
        Easier to read with collapsed conditions
        """
        first = head
        prev = None
        while first:
            first = first.next
            if n <= 0:
                prev = prev.next if prev else head
            n -= 1
        if prev and prev.next:
            prev.next = prev.next.next
            return head
        else:
            # if prev is still None, we're removing head
            return head.next

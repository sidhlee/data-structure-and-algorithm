"""
Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list, instead you will be given access 
to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Example 1:
"./delete_node_1.jpeg"

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 
after calling your function.

Example 2:
"./delete_node_2.jpeg"

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9
after calling your function.

Constraints:

The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node
"""


class Solution:
    def deleteNode(self, node):
        """
        2022-06-28T11:34:49.965Z
        Runtime: 41 ms (90%)
        Memory Usage: 14.4 MB (0%)

        Because we're givin the removing node,
        We can copy the next node into the current node and
        the original next node becomes unreferenced.
        eg. From A->B->C, remove A
        B---->C
           B -> will be garbage-picked
        """
        node.val, node.next = node.next.val, node.next.next

    def deleteNode_not_working(self, node):
        """
        This doesn't pass because we're trying to move through
        the node that are no longer 'next' of the current node.

        [2,0,1,3], 2 outputs [0, 3] instead of [0,1,3]
        './delete_node_3.png'
        - After making the first node to point to the next next node (1),
          we should't be moving to the next node (0), because that node is already detached from the previous node.
        """
        while node.next:
            node.val = node.next.val
            t = node.next
            node.next = node.next.next
            node = t

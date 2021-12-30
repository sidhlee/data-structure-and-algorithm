# Singly Linked List

Singly Linked List is a linked list where nodes are linked to the next node in a single direction.

## Singly Linked List Methods

### `push(val): SinglyLinkedList`

- creates a new node with the given value.
- If the `head` value is `null`, then set the new node to be the head, otherwise set the `next` of the tail to be the new node and update the tail.
- Finally increment the `length` by one.

### `pop(): Node | undefined`

- If there are no nodes in the list, return `undefined`
- Loop through the list until you reach the tail
- Set the `next` of the 2nd last node to be`null`
- Set the 2nd last node to be `tail`
- Decrement the `length` of the list by one
- Return the removed node

### `shift(): Node | undefined`

- If there are no nodes in the list, return `undefined`
- Store `head` value
- set head to be `head.next`
- decrement `length`
- return stored `head` value

# Singly Linked List

Singly Linked List is a linked list where nodes are linked to the next node in a single direction.

## Singly Linked List Methods

### `push(val): SinglyLinkedList`

`push` inserts a new node to the tail.

- Creates a new node with the given value.
- If the `head` value is `null`, then set the new node to be the head, otherwise set the `next` of the tail to be the new node and update the tail.
- Increment the `length` by one.
- Return the instance

### `pop(): T | undefined`

`pop` removes a node from the tail.

- If there are no nodes in the list, return `undefined`
- Loop through the list until you reach the tail
- Set the `next` of the 2nd last node to be`null`
- Set the 2nd last node to be `tail`
- Decrement the `length` of the list by one
- Return the removed node value

### `shift(): T | undefined`

`shift` removes a node from the head.

- If there are no nodes in the list, return `undefined`
- Store `head` value
- Set head to be `head.next`
- Decrement `length`
- Return stored `head` value

### `unshift(val): SinglyLinkedList`

`unshift` inserts a new node to the head.

- Creates a new node with the given value.
- If the `head` value is `null`, then set the new node to be the head, otherwise set the `next` of the new node to be the existing head and update the list's head.
- Increment the `length` by one.
- Return the instance

### `get(index): Node | undefined`

`get` finds a node at the given index

- Loop through the list until you reach the index and return the node.

### `set(val, index): SinglyLinkedList`

`set` updates the node at the given index with the value passed.

### `insert(val, index): SinglyLinkedList`

`insert` creates a new node with the given value and insert at the specified position.

- If index is 0, unshift the new node.
- If index is same as the length, push the new node.
- Otherwise, get the previous node by calling `get(index-1)`
- Set `newNode.next` to the `prevNode.next`
- Set `prevNode.next` to the new node.
- Increment `length`.
- Return the instance.

### `remove(index): Node`

`remove` deletes a node from the given position

- If the index is invalid (ie. i < 0 || i >= list.length), return `undefined`.
- If the index equals length - 1, pop.
- If the index equals 0, shift.
- Otherwise, get the previous node by calling `get(index-1)`
- Set `prevNode.next` to the `prevNode.next.next`.
- Decrement `length`.
- Return the value of the node removed.

### `reverse(): SinglyLinkedList`

`reverse` reverses the list in place.

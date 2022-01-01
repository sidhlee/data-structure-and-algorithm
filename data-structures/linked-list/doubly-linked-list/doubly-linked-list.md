# Doubly Linked List

Doubly Linked List has additional `prev` field on its nodes. This makes it more flexible than Singly Linked List, but also consumes more memory.

## Difference to the SinglyLinkedList in method implementations

### `push(val): DoublyLinkedList`

- need to set the `prev` on the newly created node and set it to either `null` (when there's no prev node) or the previous node.

### `pop(): T | undefined`

- Unlike SinglyLinkedList, there's no need for traversing to the tail - 1 to update the tail. Simply access `tail.prev` to do the job.

### `get(index): T | undefined`

- You can optimize get by iterating from the end when the index is greater than `length` / 2.

### `remove(index): T | undefined`

- Instead of getting the node at index - 1 in order to set the new tail, you can get the node being removed and use its `prev` and `next` to patch the gap.

## Doubly Linked List Complexity

- Insertion - O(1) for push and unshift
- Removal - O(1) for pop and shift. No need to iterate for updating the tail because we can use `tail.prev`
- Searching & Access - O(n) and can be optimized to O(n/2).

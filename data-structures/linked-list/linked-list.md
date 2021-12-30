# Linked List

Linked List is a data structure that has head, tail and length.
Linked List consists of nodes, and each node has a value and a pointer to another node or null.

## List vs Array

### Lists

- Indices not available
- Nodes are connected with `next` pointer
- Random access not allowed
- Faster mutation due to the lack of indexing

### Array

- Indexed
- Insertion/deletion can be expensive due to re-indexing
- Can access specific item faster with index

## Singly Linked List

Singly Linked List is a linked list where nodes are linked to the next node in a single direction.

### Singly Linked List Methods

- `push(val)` - creates a new node with the given value. If the `head` value is `null`, then set the new node to be the head, otherwise set the `next` of the tail to be the new node and update the tail. Finally increment the `length` by one.

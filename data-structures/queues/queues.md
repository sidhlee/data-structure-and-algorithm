# Queues

A queue is a FIFO data structure where the first stored item is removed first.

## Queue Applications

- Task queue
- Uploading resources

## Queue Implementations

### Queue with Array

A Queue can be implemented with Array using push/shift or unshift/pop combination. But similar to Stack, this requires re-indexing the entire array.

### Queue with SinglyLinkedList

You can use `first` and `last` property to insert and remove the item.

## Queue Complexities

- Insertion/removal - O(1) using `last` for insertion and `first` for removal
- Search/Accessing - O(n) using `next` property of the node.

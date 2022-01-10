# Stacks

A stack is a LIFO data structure where the last pushed elements is the first to be popped out.

## Stack Applications

- Managing function invocations
- Undo/Redo
- Navigating using back/forward in the browser.

## Stack Implementations

### Stack with Array

- push/pop - inserts and removes from the end
- unshift/shift - inserts and removes from the beginning. Less efficient since we need to re-index the entire array items.

### Stack with SinglyLinkedList

- You can use `shift` and `unshift` to implement stack with singly linked list, which do not require to iterate to the `last` - 1 to update the `last` with the second last element.

## Stack Complexities

- Insertion/Remove - O(1) using stacks `first` property.
- Searching/Access - O(n) using the node's `next` property.

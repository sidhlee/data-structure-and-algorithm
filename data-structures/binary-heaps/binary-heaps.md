# Binary Heaps

A Heap is a special case of a complete tree where every child has either has the value less than or equal to its parent (max heap) or greater than or equal to (min heap).

- Most commonly implemented with a binary tree
- Every line has to be filled before moving into the next level
- "one maximally efficient implementation of an abstract data type called a priority queue (wikipedia)"
- Partially sorted - the order between siblings is not guaranteed
- Often used with graph traversal algorithms

## Representing Heap with List/Array

You can represent a heap with list or array by pushing nodes from top to bottom and left to right.

```text
            14
     12             13
 11      10      8      9
1  5    7  2    3  0   4  6

[14, 12, 13, 11, 10, 8, 9, 1, 5, 7, 2, 3, 0, 4, 6]
```

With Binary Heap, there are some useful mathematical properties:

When n is the index of the parent node:

- Left child index: 2n + 1
- Right child index: 2n + 2

When n is the index of the children (left OR right):

- Parent index: Floor((n-1) / 2)

When n is the total number of nodes in the tree:

- Height of the tree : Floor(log2(n)) where the height of the single node tree is 0.

## Binary Heap Methods

### `insert(value): BinaryHeap`

Insert a value to the correct place in a tree.

- Insert the value at the end of the array
- Bubble up until finding the right spot.
  - less than its parent but greater than or equal to its children
- Compare bubbling node to its parent and swap if greater than parent.

### `extractMax(): value`

Remove the max node (root) from the heap and return it.

- Swap the root with the last node in the tree.
- Pop the root off the end of the tree and save it to return later.
- Have the new root sink down to the correct position:
  - Compare left and right child and if the bigger child is greater than the new root (parent), swap them.
  - If the bigger child is less than or equal to the new root, break out of the loop and return the saved root.

## Priority Queue

- Abstract data type
- Priority Queue is often referred to interchangeably as Heap
- In Unix, processes
- Can be implemented not only with BinaryHeap but any other data structure but likely not as efficient as heap.
- Naive implementation involves sorting nodes based on their priority.

### PQ Application

- Unix manages its processes based on their nicesness value
- At the hospitals, the most urgent patient at any given moment must be taken care of first as new patients with varying urgencies continue to be accepted.

### PQ Implementation

When a smaller number represents higher priority, we can implement a Priority Queue with Min Binary Heap.
The different from the Binary Heap would be that in priority queue, each node has value and a priority and we need to do comparison based on the priority, not the value.

## Binary Heap Complexity

- Insertion/Removal - O(log(n)) for bubbling up/down
- Search - O(n) because we still need to traverse entire list. You'd be better off using binary search tree because Binary Heap does not guarantee the order between siblings.

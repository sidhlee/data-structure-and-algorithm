# Binary Heap

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
- Compare bubbling node to its parent and swap if greater than parent.

## Priority Queue

- Abstract data type
- Often called as heap

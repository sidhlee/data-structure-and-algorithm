# Binary Tree

In Binary trees, each node can have have maximum two nodes.

## Binary Search Tree

A Binary Search Tree is a Binary Tree with sorted data where the left child always has smaller value than the parent and the right child always has a value greater than its parent.

### BST Insert

Insert with Binary Search Tree can be implemented either recursively or iteratively.

### BST Find

Finds and returns the node that matches the given value.

## BST Complexities

Binary Search Trees offer O(log(n)) time for average search, insert and delete operation where the tree is balanced.
The worst case is when the tree only has either left or right node and it's O(n) because you need to go through the entire tree to reach the leaf.

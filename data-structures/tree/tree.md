# Tree Data Structure

A Tree is a data structure consists of nodes in a parent/child relationship. Unlike the list, trees are non-linear where many paths can branch of from a single parent. We can think of a tree as a special case of tree where parents have maximum one child.

## What is NOT a tree

- sibling nodes connected to each other.
- a child node having more than one parent.

## Tree Terms

- root - a top node in a tree.
- child - a node connected to other node closer to the root.
- parent - a node connected to other node(s) farther from the root.
- siblings - nodes with the same parent.
- leaf - a node with no children.
- edge - a connection between nodes.

## Tree Applications

- HTML DOM
- Network routing
- Validating abstract syntax tree in programing languages
- Decision trees in machine learning
- File systems

## Tree Traversal

### Breadth First Search

With BFS, every sibling is visited before traversing into children.
We can use a queue and a while loop to traverse through the tree

- create an array to store visited nodes' values
- create a queue and enqueue the root
- while the queue is not empty:
  - dequeue a node and store the value into the array
  - if left is not null, enqueue left
  - if right is not null, enqueue right
- return the array with visited nodes

### Depth First Search

# Trees

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

Breadth First Search generally uses more space since it visits entire level before going deeper.

### Depth First Search

DFS is commonly implemented with recursion where each branch is traversed until it reaches the leaf node. It uses Stack data structure to push visited nodes and pop(backtrack) when there is no node to traverse.

There are two places where we can pop out of the current call stack and they are used for different purposes:

- Base case - checks at the beginning of the function if the visiting node is empty. When it returns, we go back to the leaf node.
- End of the function - after returning from left and right traversal, it pops out from the current stack to backtrack to the parent node.

### BFS vs DFS

- [Difference between BFS and DFS](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)

| BFS                                                            | DFS                                                                  |
| -------------------------------------------------------------- | -------------------------------------------------------------------- |
| Uses Queue to find the shortest path                           | Uses Stack to traverse and backtrack                                 |
| Finds the node with min # of edges                             | might traverse through more edges                                    |
| For finding node closer to root                                | For finding solution away from the root                              |
| Traverses all siblings first - not suitable for game or puzzle | Each branch is explored one after the other - good for decision tree |
| siblings before children                                       | children before sibling                                              |
| O(N + E)                                                       | O(N + E)                                                             |

# Graph Traversal

Graph traversal is different from tree traversal in that:

- it doesn't always start from the root
- it can have cycles -> need to remember already visited nodes

## Depth First Graph Traversal

"Explore as far as down the branch before backtracking"

- traverse through current node's neighbor before visiting all the sibling nodes.
- focus on deepening the traversal
- use stack data structure to backtrack
  - most recently pushed node will be popped and visited before the old ones

### DFS Recursive

Pseudo code

```text
DFS(vertex):
  if vertex is empty
    return (this is base case)
  add vertex to results list
  mark vertex as visited
  for each neighbor in vertex's neighbors:
    if neighbor is not visited:
      recursively call DFS on neighbor

```

### DFS Iterative

Pseudo code

```text
DFS(vertex):
  let S be a new stack
  S.push(vertex)
  while S is not empty
    vertex = S.pop()
    if vertex is not labelled as discovered
      visit vertex (add to the results list)
      label vertex as discovered
      for each of vertex's neighbors, N do
        S.push(N)
```

## Breadth First Graph Traversal

"Visit neighbors at the current depth first"

- focus on broadening the traversal
- use queue data structure to visit nodes in order
  - new nodes can be enqueued, but nodes are visited in queueing order.

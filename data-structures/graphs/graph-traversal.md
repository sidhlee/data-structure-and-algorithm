# Graph Traversal

Graph traversal is different from tree traversal in that:

- it doesn't always start from the root
- it can have cycles -> need to remember already visited

## Depth First Graph Traversal

"Explore as far as down the branch before "backtracking"

- traverse through current node's neighbor before visiting all the sibling nodes.

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

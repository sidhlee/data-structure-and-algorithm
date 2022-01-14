# Graph Traversal

Graph traversal is different from tree traversal in that:

- it doesn't always start from the root
- it can have cycles -> need to remember already visited

## Depth First Graph Traversal

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

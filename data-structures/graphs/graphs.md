# Graphs

A **Graph** data structure has `vertices`(nodes or points) connected with `edges`.

- A tree data structure is a special case of graphs.
- Two vertices connected with an edge can be ordered in `directed graph` or unordered in `undirected graph`. (eg. follow members in one or both directions)
- Edges can be `weighted` or `unweighted` (eg. distance between two cities)

## Graph Applications

- SNS - **connections** between members
- Map/geo-location (eg. finding a shortest **path**)
- Recommendation algorithms (eg. Netflix, Amazon, etc..)
- File system optimizations
- Routing algorithms
- Internet

## Graph Implementations

### Adjacency List

With an adjacency list, every vertex keeps a list of connected vertices.

- less space than adjacency matrix (linear vs quadratic)
- slower search by iterating through vertices and edges

### Adjacency Matrix

An adjacency matrix is a n \* n matrix where you can assign 1 or 0 to represent the connection between vertices. Undirected graph will always have the same value at the `cell[i][j]` and `cell[j][i]`. When implemented with array, the length of the outer array will be same as the length of the inner array.

- faster lookup by row & column index
- quadratic space - not suitable for sparse edges

## Graph Complexities

**\|V\|** - number of vertices, **\|E\|** - number od edges

| OPERATION     | ADJACENCY LIST                                                                                                       | ADJACENCY MATRIX                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Add Vertex    | O(1) for adding a new list to the outer array                                                                        | O(\|V^2\|) for copying the whole matrix to the new (n+1)^2 matrix |
| Add Edge      | O(1) for adding connected vertex to the list                                                                         | O(1) for writing 1 to `matrix[i][j]`                              |
| Remove Vertex | O(\|V\| + \|E\|) for finding vertex (this will be constant if hash table is used) AND updating all edges in the list | O(\|V ^2\| for copying the whole matrix to the new matrix         |
| Remove Edge   | O(\|E\|)                                                                                                             | O(1)                                                              |
| Query         | O(\|V\| + \|E\|)                                                                                                     | O(1)                                                              |
| Storage       | O(\|V\| + \|E\|)                                                                                                     | O(\|V^2\|)                                                        |

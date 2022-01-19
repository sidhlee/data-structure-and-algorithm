# Dijkstra's Algorithm

Dijkstra's Algorithm finds the shortest path from the **source** to **all vertices** in a given graph where all the edges have positive weights (ie. we know all the distances between nodes). It uses a **priority queue** to access the node with the smallest distance from the source and update the distances of all its **neighbors** by summing up its own distance from the source and the weight of the edge to that neighbor. All vertices in the graphs start with the initial weight of the **positive infinity**, and only updates when the new value is smaller than the current value. We also keep track of the **visited nodes** to avoid cycling.

## Dijkstra's Pseudocode

```text
dijkstra(startNode: Vertex, finishNode: Vertex):
  - create distanceDict with vertices in adjacencyList and set the initial value of Infinity except for the starting node which will have 0 as the distance.
  - add all vertices except the starting node to the priority queue (nextVisitingNode) with the priority being the distance.
  - create prevNodeDict with vertices and set initial values of null.
  - while pq.size > 0:
    - dequeue visitingNode from pq
    - break if visitingNode == finishNode
    - else loop through visitingNode's adjacency list:
      - get the distance of the neighbor from startNode
      - only if the distance < distanceDict[neighbor]
        - update distanceDict with new distance
        - update prevNodeDict
        - enqueue(neighbor, distance)
```

## TODO

- Add complexities
- Add optimizations

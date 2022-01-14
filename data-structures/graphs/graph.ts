type Vertex = string;

export class Graph {
  adjacencyLists: { [vertex: string]: Vertex[] };
  constructor() {
    this.adjacencyLists = {};
  }

  addVertex(vertex: string) {
    if (!this.adjacencyLists[vertex]) {
      this.adjacencyLists[vertex] = [];
    }
  }

  addEdge(vertex1: Vertex, vertex2: Vertex) {
    if (!this.adjacencyLists[vertex1] || !this.adjacencyLists[vertex2]) return;
    this.adjacencyLists[vertex1].push(vertex2);
    this.adjacencyLists[vertex2].push(vertex1);
  }

  removeEdge(vertex1: Vertex, vertex2: Vertex) {
    if (!this.adjacencyLists[vertex1] || !this.adjacencyLists[vertex2]) return;
    this.adjacencyLists[vertex1] = this.adjacencyLists[vertex1].filter(
      (v) => v !== vertex2
    );
    this.adjacencyLists[vertex2] = this.adjacencyLists[vertex2].filter(
      (v) => v !== vertex1
    );
  }

  removeVertex(vertex: Vertex) {
    const edges = this.adjacencyLists[vertex];
    if (!edges) return;
    for (const edge of edges) {
      this.removeEdge(vertex, edge);
    }
    delete this.adjacencyLists[vertex];
  }

  traverseDepthFirstRecursively(startingNode: Vertex) {
    const adjacencyLists = this.adjacencyLists;
    const traversedNodeList = [] as Vertex[];
    const visitedNodesDict = {} as { [node: string]: boolean };

    function traverse(fromNode: Vertex) {
      if (!fromNode) return;
      traversedNodeList.push(fromNode);
      visitedNodesDict[fromNode] = true;
      for (const node of adjacencyLists[fromNode]) {
        if (!visitedNodesDict[node]) {
          traverse(node);
        } else continue;
      }
      return;
    }
    if (adjacencyLists[startingNode]) {
      traverse(startingNode);
    }

    return traversedNodeList;
  }
}

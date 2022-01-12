type Vertex = string;

export class Graph {
  adjacencyList: { [vertex: string]: Vertex[] };
  constructor() {
    this.adjacencyList = {};
  }

  addVertex(vertex: string) {
    if (!this.adjacencyList[vertex]) {
      this.adjacencyList[vertex] = [];
    }
  }

  addEdge(vertex1: Vertex, vertex2: Vertex) {
    if (!this.adjacencyList[vertex1] || !this.adjacencyList[vertex2]) return;
    this.adjacencyList[vertex1].push(vertex2);
    this.adjacencyList[vertex2].push(vertex1);
  }

  removeEdge(vertex1: Vertex, vertex2: Vertex) {
    if (!this.adjacencyList[vertex1] || !this.adjacencyList[vertex2]) return;
    this.adjacencyList[vertex1] = this.adjacencyList[vertex1].filter(
      (v) => v !== vertex2
    );
    this.adjacencyList[vertex2] = this.adjacencyList[vertex2].filter(
      (v) => v !== vertex1
    );
  }

  removeVertex(vertex: Vertex) {
    const edges = this.adjacencyList[vertex];
    if (!edges) return;
    for (const edge of edges) {
      this.removeEdge(vertex, edge);
    }
    delete this.adjacencyList[vertex];
  }
}

import { Queue } from '../queues/queue';
import { Stack } from '../stacks/stack';

type Vertex = string;
type AdjacencyLists = { [vertex: string]: any[] };

abstract class Graph {
  adjacencyLists: AdjacencyLists;
  constructor() {
    this.adjacencyLists = {};
  }

  addVertex(vertex: string) {
    if (!this.adjacencyLists[vertex]) {
      this.adjacencyLists[vertex] = [];
    }
  }

  abstract addEdge(vertex1: Vertex, vertex2: Vertex, weight?: number): void;

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
}

type UnweightedAdjacencyLists = { [vertex: string]: string[] };

export class UnweightedGraph extends Graph {
  // declare allows to override Super field without compiling into JS:
  // https://stackoverflow.com/a/70060417
  declare adjacencyLists: UnweightedAdjacencyLists;
  addEdge(vertex1: Vertex, vertex2: Vertex) {
    if (!this.adjacencyLists[vertex1] || !this.adjacencyLists[vertex2]) return;
    this.adjacencyLists[vertex1].push(vertex2);
    this.adjacencyLists[vertex2].push(vertex1);
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

  traverseDepthFirstIteratively(startingNode: Vertex) {
    if (!this.adjacencyLists[startingNode]) return [];

    const traversedNodeList = [] as Vertex[];
    const visitedNodesDict = {} as { [node: string]: boolean };
    const stack = new Stack<Vertex>();
    stack.push(startingNode);
    // we're only marking neighbors inside the loop
    // so we need to mark the starting node here
    visitedNodesDict[startingNode] = true;

    while (stack.size > 0) {
      const poppedNode = stack.pop();
      if (poppedNode) {
        traversedNodeList.push(poppedNode);
        this.adjacencyLists[poppedNode].forEach((neighbor) => {
          if (!visitedNodesDict[neighbor]) {
            visitedNodesDict[neighbor] = true;
            stack.push(neighbor);
          }
        });
      }
    }
    return traversedNodeList;
  }

  traverseBreadthFirst(startingNode: Vertex) {
    if (!this.adjacencyLists[startingNode]) return [];

    const traversedNodeList = [] as Vertex[];
    const visitedNodesDict = {} as { [node: string]: boolean };
    const queue = new Queue<Vertex>();
    queue.enqueue(startingNode);
    visitedNodesDict[startingNode] = true;

    while (queue.size > 0) {
      const currentNode = queue.dequeue();
      if (currentNode) {
        traversedNodeList.push(currentNode);
        this.adjacencyLists[currentNode].forEach((neighbor) => {
          if (!visitedNodesDict[neighbor]) {
            visitedNodesDict[neighbor] = true;
            queue.enqueue(neighbor);
          }
        });
      }
    }
    return traversedNodeList;
  }
}

class WeightedEdge {
  constructor(public node: string, public weight: number) {}
}

type WeightedAdjacencyLists = { [vertex: string]: WeightedEdge[] };

export class WeightedGraph extends Graph {
  declare adjacencyLists: WeightedAdjacencyLists;

  addEdge(vertex1: string, vertex2: string, weight: number): void {
    if (!this.adjacencyLists[vertex1] || !this.adjacencyLists[vertex2]) return;

    this.adjacencyLists[vertex1].push(new WeightedEdge(vertex2, weight));
    this.adjacencyLists[vertex2].push(new WeightedEdge(vertex1, weight));
  }
}

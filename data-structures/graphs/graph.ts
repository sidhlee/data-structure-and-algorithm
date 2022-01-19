import { PriorityQueue } from '../binary-heaps/priorityQueue';
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

  getShortestPathWithDijkstra(startNode: Vertex, finishNode: Vertex): Vertex[] {
    // handle edge cases
    if (startNode === finishNode) return [startNode];
    // return empty array if startNode and/or finishNode is an island (and they're not the same node)
    if (
      this.adjacencyLists[startNode].length === 0 ||
      this.adjacencyLists[finishNode].length === 0
    )
      return [];

    // create & initialize data stores
    const distanceDict = {} as { [vertex: string]: number };
    const visitedNodesDict = {} as { [vertex: string]: boolean };
    const prevNodeDict = {} as { [vertex: string]: string | null };
    const shortestDistanceNodeQueue = new PriorityQueue();

    for (const vertex in this.adjacencyLists) {
      const distance = vertex === startNode ? 0 : Infinity;
      distanceDict[vertex] = distance;
      // shortestDistanceNodeQueue.enqueue(vertex, distance);
      prevNodeDict[vertex] = null;
      visitedNodesDict[vertex] = false;
    }
    // still work if we initialize PQ with only start node.
    shortestDistanceNodeQueue.enqueue(startNode, 0);

    // repeat until the queue is exhausted
    while (shortestDistanceNodeQueue.nodes.length > 0) {
      const visitingNode = shortestDistanceNodeQueue.dequeue();
      // for typechecking
      if (!visitingNode) return [];

      const visitingNodeName = visitingNode.value;
      const visitingNodeDistance = visitingNode.priority;

      // break if reached to the finish node
      if (visitingNodeName === finishNode) {
        break;
      }

      // Colt also checks whether the visitingNode has Infinity in distanceDict
      // but this was not explained and don't understand why it's necessary
      // TODO: check out other dijkstra implementations
      if (visitingNode) {
        visitedNodesDict[visitingNodeName] = true;
        this.adjacencyLists[visitingNodeName].forEach((edge) => {
          const neighborHasNotBeenVisited = !visitedNodesDict[edge.node];

          if (neighborHasNotBeenVisited) {
            const neighborNodeName = edge.node;
            const neighborNodeDistance = visitingNodeDistance + edge.weight;

            // only update stores if the current path has shorter distance than the existing one.
            if (neighborNodeDistance < distanceDict[neighborNodeName]) {
              distanceDict[neighborNodeName] = neighborNodeDistance;
              prevNodeDict[neighborNodeName] = visitingNodeName;
              // we're enqueueing instead of updating existing no in the queue
              // because enqueueing(constant time) is much cheaper than lookup (linear time)
              shortestDistanceNodeQueue.enqueue(
                neighborNodeName,
                neighborNodeDistance
              );
            }
          }
        });
      }
    }

    const shortestPath = [finishNode] as Vertex[];

    while (true) {
      const currentNode = shortestPath[0];
      const prevNode = prevNodeDict[currentNode];
      if (prevNode) {
        shortestPath.unshift(prevNode);
      } else {
        break;
      }
    }

    return shortestPath;
  }
}

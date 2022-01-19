import { UnweightedGraph, WeightedGraph } from './graph';

describe('UnweightedGraph', () => {
  let graph: UnweightedGraph;
  beforeEach(() => {
    graph = new UnweightedGraph();
  });
  it('has adjacency list', () => {
    expect(graph.adjacencyLists).not.toBeUndefined();
  });
  describe('addVertex', () => {
    it('creates new key and an empty list to adjacency list', () => {
      graph.addVertex('Neo');
      expect(graph.adjacencyLists['Neo']).toEqual([]);
    });

    it('should do nothing if there is an existing vertex', () => {
      const existingList = ['Trinity', 'Morpheus'];
      graph.adjacencyLists = { Neo: existingList };
      graph.addVertex('Neo');
      expect(graph.adjacencyLists['Neo']).toEqual(existingList);
    });
  });

  describe('addEdge', () => {
    beforeEach(() => {
      graph.adjacencyLists = {
        Neo: [],
        Trinity: [],
      };
    });
    it('should do nothing if vertices are not found', () => {
      graph = new UnweightedGraph();
      graph.addEdge('Smith', 'Architect');
      expect(graph.adjacencyLists).toEqual({});
    });
    it('should add vertex2 to the vertex1 list', () => {
      graph.addEdge('Neo', 'Trinity');
      expect(graph.adjacencyLists['Neo']).toEqual(['Trinity']);
    });

    it('should add vertex1 to the vertex2 list', () => {
      graph.addEdge('Neo', 'Trinity');
      expect(graph.adjacencyLists['Trinity']).toEqual(['Neo']);
    });
  });

  describe('removeEdge', () => {
    beforeEach(() => {
      graph.adjacencyLists = {
        Neo: ['Trinity', 'Morpheus'],
        Trinity: ['Neo', 'Morpheus'],
        Morpheus: ['Neo', 'Trinity'],
      };
    });
    it('should do nothing if vertices are not found', () => {
      graph.removeEdge('Smith', 'Neo');
      expect(graph.adjacencyLists).toEqual({
        Neo: ['Trinity', 'Morpheus'],
        Trinity: ['Neo', 'Morpheus'],
        Morpheus: ['Neo', 'Trinity'],
      });
    });

    it('should remove vertex2 from the vertex1 list', () => {
      graph.removeEdge('Neo', 'Trinity');
      expect(graph.adjacencyLists['Neo']).toEqual(['Morpheus']);
    });

    it('should remove vertex1 from the vertex2 list', () => {
      graph.removeEdge('Neo', 'Trinity');
      expect(graph.adjacencyLists['Trinity']).toEqual(['Morpheus']);
    });
  });

  describe('removeVertex', () => {
    beforeEach(() => {
      graph.adjacencyLists = {
        Neo: ['Trinity', 'Morpheus'],
        Trinity: ['Neo', 'Morpheus'],
        Morpheus: ['Neo', 'Trinity'],
      };
    });
    it('should remove vertex', () => {
      graph.removeVertex('Neo');
      expect(graph.adjacencyLists['Neo']).toBeUndefined();
    });

    it('should remove edges', () => {
      graph.removeVertex('Neo');
      expect(graph.adjacencyLists['Trinity']).toEqual(['Morpheus']);
      expect(graph.adjacencyLists['Morpheus']).toEqual(['Trinity']);
    });

    it('should do nothing if the vertex does not exist', () => {
      graph.removeVertex('Smith');
      expect(graph.adjacencyLists).toEqual({
        Neo: ['Trinity', 'Morpheus'],
        Trinity: ['Neo', 'Morpheus'],
        Morpheus: ['Neo', 'Trinity'],
      });
    });
  });

  describe('traverseDepthFirstRecursively', () => {
    let graph: UnweightedGraph;
    beforeEach(() => {
      graph = new UnweightedGraph();
      graph.addVertex('A');
      graph.addVertex('B');
      graph.addVertex('C');
      graph.addVertex('D');
      graph.addVertex('E');
      graph.addVertex('F');

      graph.addEdge('A', 'B');
      graph.addEdge('A', 'C');
      graph.addEdge('B', 'D');
      graph.addEdge('C', 'E');
      graph.addEdge('D', 'E');
      graph.addEdge('D', 'F');
      graph.addEdge('E', 'F');
    });
    it('returns the correct result starting from the first node', () => {
      expect(graph.traverseDepthFirstRecursively('A')).toEqual([
        'A',
        'B',
        'D',
        'E',
        'C',
        'F',
      ]);
    });

    it('returns the correct result starting from the last node', () => {
      expect(graph.traverseDepthFirstRecursively('F')).toEqual([
        'F',
        'D',
        'B',
        'A',
        'C',
        'E',
      ]);
    });

    it('returns an empty array when given an invalid node', () => {
      expect(graph.traverseDepthFirstRecursively('Z')).toEqual([]);
    });
  });

  describe('traverseDepthFirstIteratively', () => {
    let graph: UnweightedGraph;
    beforeEach(() => {
      graph = new UnweightedGraph();
      graph.addVertex('A');
      graph.addVertex('B');
      graph.addVertex('C');
      graph.addVertex('D');
      graph.addVertex('E');
      graph.addVertex('F');

      graph.addEdge('A', 'B');
      graph.addEdge('A', 'C');
      graph.addEdge('B', 'D');
      graph.addEdge('C', 'E');
      graph.addEdge('D', 'E');
      graph.addEdge('D', 'F');
      graph.addEdge('E', 'F');
    });
    it('returns the correct result starting from the first node', () => {
      expect(graph.traverseDepthFirstIteratively('A')).toEqual([
        'A',
        'C',
        'E',
        'F',
        'D',
        'B',
      ]);
    });

    it('returns the correct result starting from the last node', () => {
      expect(graph.traverseDepthFirstIteratively('F')).toEqual([
        'F',
        'E',
        'C',
        'A',
        'B',
        'D',
      ]);
    });

    it('returns an empty array when given an invalid node', () => {
      expect(graph.traverseDepthFirstIteratively('Z')).toEqual([]);
    });
  });

  describe('traverseBreadthFirst', () => {
    let graph: UnweightedGraph;
    beforeEach(() => {
      graph = new UnweightedGraph();
      graph.addVertex('A');
      graph.addVertex('B');
      graph.addVertex('C');
      graph.addVertex('D');
      graph.addVertex('E');
      graph.addVertex('F');

      graph.addEdge('A', 'B');
      graph.addEdge('A', 'C');
      graph.addEdge('B', 'D');
      graph.addEdge('C', 'E');
      graph.addEdge('D', 'E');
      graph.addEdge('D', 'F');
      graph.addEdge('E', 'F');
    });
    it('returns the correct result starting from the first node', () => {
      expect(graph.traverseBreadthFirst('A')).toEqual([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
      ]);
    });

    it('returns the correct result starting from the last node', () => {
      expect(graph.traverseBreadthFirst('F')).toEqual([
        'F',
        'D',
        'E',
        'B',
        'C',
        'A',
      ]);
    });

    it('returns an empty array when given an invalid node', () => {
      expect(graph.traverseBreadthFirst('Z')).toEqual([]);
    });
  });
});

describe('WeightedGraph', () => {
  let graph: WeightedGraph;
  beforeEach(() => {
    graph = new WeightedGraph();
    graph.addVertex('A');
    graph.addVertex('B');
    graph.addVertex('C');
    graph.addVertex('D');
    graph.addVertex('E');
    graph.addVertex('F');
  });
  describe('addEdge', () => {
    it('adds weighted edges to both vertices', () => {
      graph.addEdge('A', 'B', 5);
      expect(graph.adjacencyLists['A']).toEqual([{ node: 'B', weight: 5 }]);
      expect(graph.adjacencyLists['B']).toEqual([{ node: 'A', weight: 5 }]);
    });

    it('does not do anything for invalid vertices', () => {
      graph.addEdge('A', 'invalid', 5);
      graph.addEdge('invalid', 'B', 5);
      graph.addEdge('invalid', 'invalid', 5);
      expect(graph.adjacencyLists['A']).toEqual([]);
      expect(graph.adjacencyLists['B']).toEqual([]);
    });
  });

  describe('getShortestPathWithDijkstra', () => {
    beforeEach(() => {
      graph.addEdge('A', 'B', 4);
      graph.addEdge('A', 'C', 2);
      graph.addEdge('B', 'E', 3);
      graph.addEdge('C', 'D', 2);
      graph.addEdge('C', 'F', 4);
      graph.addEdge('D', 'E', 3);
      graph.addEdge('D', 'F', 1);
      graph.addEdge('E', 'F', 1);
    });
    it('returns shortest path array', () => {
      expect(graph.getShortestPathWithDijkstra('A', 'E')).toEqual([
        'A',
        'C',
        'D',
        'F',
        'E',
      ]);
    });

    it('works with island', () => {
      graph.addVertex('island');
      expect(graph.getShortestPathWithDijkstra('A', 'E')).toEqual([
        'A',
        'C',
        'D',
        'F',
        'E',
      ]);
    });
  });
});

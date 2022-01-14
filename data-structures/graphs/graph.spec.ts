import { Graph } from './graph';

describe('Graph', () => {
  let graph: Graph;
  beforeEach(() => {
    graph = new Graph();
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
      graph = new Graph();
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
    let graph: Graph;
    beforeEach(() => {
      graph = new Graph();
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
});

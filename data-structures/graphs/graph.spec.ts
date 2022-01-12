import { Graph } from './graph';

describe('Graph', () => {
  let graph: Graph;
  beforeEach(() => {
    graph = new Graph();
  });
  it('has adjacency list', () => {
    expect(graph.adjacencyList).not.toBeUndefined();
  });
  describe('addVertex', () => {
    it('creates new key and an empty list to adjacency list', () => {
      graph.addVertex('Neo');
      expect(graph.adjacencyList['Neo']).toEqual([]);
    });

    it('should do nothing if there is an existing vertex', () => {
      const existingList = ['Trinity', 'Morpheus'];
      graph.adjacencyList = { Neo: existingList };
      graph.addVertex('Neo');
      expect(graph.adjacencyList['Neo']).toEqual(existingList);
    });
  });

  describe('addEdge', () => {
    beforeEach(() => {
      graph.adjacencyList = {
        Neo: [],
        Trinity: [],
      };
    });
    it('should do nothing if vertices are not found', () => {
      graph = new Graph();
      graph.addEdge('Smith', 'Architect');
      expect(graph.adjacencyList).toEqual({});
    });
    it('should add vertex2 to the vertex1 list', () => {
      graph.addEdge('Neo', 'Trinity');
      expect(graph.adjacencyList['Neo']).toEqual(['Trinity']);
    });

    it('should add vertex1 to the vertex2 list', () => {
      graph.addEdge('Neo', 'Trinity');
      expect(graph.adjacencyList['Trinity']).toEqual(['Neo']);
    });
  });

  describe('removeEdge', () => {
    beforeEach(() => {
      graph.adjacencyList = {
        Neo: ['Trinity', 'Morpheus'],
        Trinity: ['Neo', 'Morpheus'],
        Morpheus: ['Neo', 'Trinity'],
      };
    });
    it('should do nothing if vertices are not found', () => {
      graph.removeEdge('Smith', 'Neo');
      expect(graph.adjacencyList).toEqual({
        Neo: ['Trinity', 'Morpheus'],
        Trinity: ['Neo', 'Morpheus'],
        Morpheus: ['Neo', 'Trinity'],
      });
    });

    it('should remove vertex2 from the vertex1 list', () => {
      graph.removeEdge('Neo', 'Trinity');
      expect(graph.adjacencyList['Neo']).toEqual(['Morpheus']);
    });

    it('should remove vertex1 from the vertex2 list', () => {
      graph.removeEdge('Neo', 'Trinity');
      expect(graph.adjacencyList['Trinity']).toEqual(['Morpheus']);
    });
  });

  describe('removeVertex', () => {
    beforeEach(() => {
      graph.adjacencyList = {
        Neo: ['Trinity', 'Morpheus'],
        Trinity: ['Neo', 'Morpheus'],
        Morpheus: ['Neo', 'Trinity'],
      };
    });
    it('should remove vertex', () => {
      graph.removeVertex('Neo');
      expect(graph.adjacencyList['Neo']).toBeUndefined();
    });

    it('should remove edges', () => {
      graph.removeVertex('Neo');
      expect(graph.adjacencyList['Trinity']).toEqual(['Morpheus']);
      expect(graph.adjacencyList['Morpheus']).toEqual(['Trinity']);
    });

    it('should do nothing if the vertex does not exist', () => {
      graph.removeVertex('Smith');
      expect(graph.adjacencyList).toEqual({
        Neo: ['Trinity', 'Morpheus'],
        Trinity: ['Neo', 'Morpheus'],
        Morpheus: ['Neo', 'Trinity'],
      });
    });
  });
});

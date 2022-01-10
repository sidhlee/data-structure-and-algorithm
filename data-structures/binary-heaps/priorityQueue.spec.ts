import { PriorityQueue, Node } from './priorityQueue';

/**
 * returns priority queue filled with nodes
 * @param values values or the nodes. priority will be set with the index of each item
 */
function priorityQueueFactory(values: any[]) {
  const pq = new PriorityQueue();
  values.forEach((val, i) => {
    const node = new Node(val, i);
    pq.nodes.push(node);
  });
  return pq;
}

describe('PriorityQueue', () => {
  describe('enqueue', () => {
    let pq: PriorityQueue;
    beforeEach(() => {
      pq = new PriorityQueue();
    });
    it('works with empty queue', () => {
      pq.enqueue('one', 1);
      expect(pq.nodes[0].value).toBe('one');
      expect(pq.nodes[0].priority).toBe(1);
    });

    it('works with one node', () => {
      const zero = new Node('zero', 0);
      const one = new Node('one', 1);
      pq.nodes.push(one);
      pq.enqueue('zero', 0);
      const expectedNodes = [zero, one];
      expect(pq.nodes).toEqual(expectedNodes);
    });

    it('works with many nodes', () => {
      const zero = new Node('zero', 0);
      const one = new Node('one', 1);
      const two = new Node('two', 2);
      const three = new Node('three', 3);
      const four = new Node('four', 4);
      const five = new Node('five', 5);
      pq.nodes = [zero, one, three, four, five];
      pq.enqueue('two', 2);
      // order between siblings is not guaranteed
      const expectedNodes = [zero, one, two, four, five, three];
      expect(pq.nodes).toEqual(expectedNodes);
    });
  });

  describe('dequeue', () => {
    let pq: PriorityQueue;
    beforeEach(() => {
      pq = new PriorityQueue();
    });
    it('returns undefined when the queue is empty', () => {
      const pq = new PriorityQueue();
      expect(pq.dequeue()).toBe(undefined);
    });

    it('returns the node with the min priority value', () => {
      const zero = new Node('zero', 0);
      const one = new Node('one', 1);
      const two = new Node('two', 2);
      const three = new Node('three', 3);
      const four = new Node('four', 4);
      const five = new Node('five', 5);
      const nodes = [zero, one, two, three, four, five];
      pq.nodes = nodes;
      const minPriorityNode = nodes
        .slice()
        .sort((a, b) => a.priority - b.priority)[0];

      const dequeued = pq.dequeue();
      expect(dequeued).toEqual(minPriorityNode);
    });

    it('keeps priority queue ordered', () => {
      const zero = new Node('zero', 0);
      const one = new Node('one', 1);
      const two = new Node('two', 2);
      const three = new Node('three', 3);
      const four = new Node('four', 4);
      const five = new Node('five', 5);
      const nodes = [zero, one, two, three, four, five];
      pq.nodes = nodes;
      pq.dequeue();
      const nodePriorities = pq.nodes.map((node) => node.priority);
      expect(nodePriorities).toEqual([1, 3, 2, 5, 4]);
    });

    it('works with single node', () => {
      const node = new Node('item', 52);
      pq.nodes = [node];
      const dequeuedNode = pq.dequeue();
      expect(dequeuedNode).toEqual(node);
      expect(pq.nodes).toEqual([]);
    });

    it("doesn't break with an empty pq", () => {
      pq.nodes = [];
      expect(pq.dequeue()).toBe(undefined);
    });
  });
});

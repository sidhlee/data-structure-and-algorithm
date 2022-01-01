import { Queue } from './queue';

describe('Queue', () => {
  it('has first, last and size', () => {
    const queue = new Queue();
    expect(queue.first).not.toBeUndefined();
    expect(queue.last).not.toBeUndefined();
    expect(queue.size).not.toBeUndefined();
  });

  describe('enqueue', () => {
    let queue: Queue<string>;
    beforeEach(() => {
      queue = new Queue<string>();
    });

    it('set the new node as first and last if there is no node', () => {
      queue.enqueue('item');
      expect(queue.first?.value).toBe('item');
      expect(queue.last?.value).toBe('item');
    });

    it(`sets the old last's next and last to be new node`, () => {
      queue.enqueue('first');
      queue.enqueue('second');
      expect(queue.first?.next?.value).toBe('second');
      expect(queue.last?.value).toBe('second');
    });

    it('increments the size by one', () => {
      expect(queue.size).toBe(0);
      queue.enqueue('item');
      expect(queue.size).toBe(1);
    });

    it('returns the new size', () => {
      expect(queue.enqueue('item')).toBe(1);
    });
  });

  describe('dequeue', () => {
    it('returns null if there is no node', () => {
      expect(new Queue().dequeue()).toBeNull();
    });

    it('set the first and last to be null if there was only one node', () => {
      const queue = new Queue();
      queue.enqueue('only item');
      queue.dequeue();
      expect(queue.first).toBe(null);
      expect(queue.last).toBe(null);
    });

    it('sets the next of the first to be the new first', () => {
      const queue = new Queue();
      queue.enqueue('first');
      queue.enqueue('second');
      expect(queue.first?.next?.value).toBe('second');
      queue.dequeue();
      expect(queue.first?.value).toBe('second');
    });

    it('decrements the size by 1', () => {
      const queue = new Queue();
      queue.enqueue('first');
      expect(queue.size).toBe(1);
      queue.dequeue();
      expect(queue.size).toBe(0);
    });

    it('returns the value of the node dequeued', () => {
      const queue = new Queue();
      queue.enqueue('first');
      queue.enqueue('second');
      expect(queue.dequeue()).toBe('first');
    });
  });
});

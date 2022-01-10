import { Stack } from './stack';

describe('Stack', () => {
  it('has first, last and size', () => {
    const stack = new Stack();
    expect(stack.first).not.toBeUndefined();
    expect(stack.last).not.toBeUndefined();
    expect(stack.size).not.toBeUndefined();
  });
  describe('push', () => {
    it('increments size', () => {
      const stack = new Stack();
      stack.push(1);
      expect(stack.size).toBe(1);
    });
    it('sets first and last', () => {
      const stack = new Stack();
      stack.push(1);
      stack.push(2);
      expect(stack.first?.value).toBe(1);
      expect(stack.last?.value).toBe(2);
    });
  });

  describe('pop', () => {
    let stack: Stack<string>;
    beforeEach(() => {
      stack = new Stack<string>();
    });
    it('returns null if there is no nodes', () => {
      expect(stack.pop()).toBe(null);
    });
    it('sets first and last to null after removing only node', () => {
      stack.push('only item');
      stack.pop();
      expect(stack.first).toBeNull();
      expect(stack.last).toBeNull();
    });
    it('sets the second item to be first when there there is more than one node', () => {
      stack.push('first');
      stack.push('second');
      stack.pop();
      expect(stack.first?.value).toBe('second');
    });
    it('decreases the size by one', () => {
      stack.push('first');
      expect(stack.size).toBe(1);
      stack.pop();
      expect(stack.size).toBe(0);
    });
    it('returns the value of the node removed', () => {
      stack.push('first');
      expect(stack.pop()).toBe('first');
    });
  });
});

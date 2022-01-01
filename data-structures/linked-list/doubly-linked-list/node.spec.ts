import Node from './node';

describe('Node', () => {
  it('should have value, prev and next', () => {
    const node = new Node(1);
    expect(node.val).not.toBeUndefined();
    expect(node.prev).not.toBeUndefined();
    expect(node.next).not.toBeUndefined();
  });

  it('can be linked to the next node', () => {
    const first = new Node(1);
    const second = new Node(2);
    const third = new Node(3);
    first.next = second;
    second.next = third;
    expect(first.next.next).toBe(third);
  });

  it('can be linked to the prev node', () => {
    const first = new Node(1);
    const second = new Node(2);
    const third = new Node(3);
    third.prev = second;
    second.prev = first;
    expect(third.prev.prev).toBe(first);
  });
});

import Node from './node';

// jest.mock('./node', () => {
//   return jest.fn().mockImplementation(() => {
//     return {};
//   });
// });

describe('Node', () => {
  it('should have value and next', () => {
    const node = new Node(1);
    expect(node.val).not.toBeUndefined();
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
});

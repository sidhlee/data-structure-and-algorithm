import { MaxBinaryHeap } from './binaryHeap';

describe('MaxBinaryHeap', () => {
  it('inserts value at the correct position', () => {
    const heap = new MaxBinaryHeap();
    heap.insert(100).insert(50).insert(70).insert(30);
    heap.insert(60);
    expect(heap.values).toEqual([100, 60, 70, 30, 50]);
  });

  it('should work for duplicated values', () => {
    const heap = new MaxBinaryHeap();
    heap.insert(10).insert(10).insert(10).insert(10);
    heap.insert(11);
    expect(heap.values).toEqual([11, 10, 10, 10, 10]);
  });
});

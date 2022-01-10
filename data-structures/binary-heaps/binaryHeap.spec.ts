import { MaxBinaryHeap } from './binaryHeap';

describe('MaxBinaryHeap', () => {
  it('has values array', () => {
    const heap = new MaxBinaryHeap();
    expect(Array.isArray(heap.values)).toBe(true);
  });
  describe('insert', () => {
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

  describe('extractMax', () => {
    let heap: MaxBinaryHeap;
    beforeEach(() => {
      heap = new MaxBinaryHeap();
      heap.values = [50, 40, 45, 30, 25, 43, 18, 25, 10, 20];
    });
    it('returns undefined when heap is empty', () => {
      const heap = new MaxBinaryHeap();
      expect(heap.extractMax()).toBe(undefined);
    });

    it('returns the max node', () => {
      expect(heap.extractMax()).toBe(50);
      expect(heap.extractMax()).toBe(45);
    });

    it('keeps max heap invariant', () => {
      heap.extractMax();
      expect(heap.values).toEqual([45, 40, 43, 30, 25, 20, 18, 25, 10]);
      heap.extractMax();
      expect(heap.values).toEqual([43, 40, 20, 30, 25, 10, 18, 25]);
    });

    it('works with single node', () => {
      heap.values = [1];
      const max = heap.extractMax();
      expect(max).toBe(1);
      expect(heap.values).toEqual([]);
    });

    it("doesn't break with an empty heap", () => {
      heap.values = [];
      expect(heap.extractMax()).toBe(undefined);
    });
  });
});
//   100
//  50  40
// 10 15

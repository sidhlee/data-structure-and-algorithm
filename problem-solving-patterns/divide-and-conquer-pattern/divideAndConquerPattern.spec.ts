import { binarySearch } from './divideAndConquerPattern';

describe('binarySearch', () => {
  it('finds the index of the value when the value is in the middle', () => {
    const result = binarySearch([1, 2, 3, 4, 5, 6], 4);
    expect(result).toBe(3);
  });

  it('finds the index of the value when the value is at the end', () => {
    const result2 = binarySearch([1, 2, 3, 4, 5, 6], 6);
    expect(result2).toBe(5);
  });

  it('returns -1 when the value is not found', () => {
    const result = binarySearch([1, 2, 3, 4, 5, 6], 7);
    expect(result).toBe(-1);
  });
});

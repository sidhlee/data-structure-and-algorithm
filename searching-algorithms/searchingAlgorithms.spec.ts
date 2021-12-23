import {
  linearSearch,
  binarySearch,
  nativeStringSearch,
} from './searchingAlgorithms';

describe('linearSearch', () => {
  it('should return found index', () => {
    expect(linearSearch([3, 1, 2], 1)).toBe(1);
  });

  it('should return -1 if not found', () => {
    expect(linearSearch([3, 1, 2], 4)).toBe(-1);
  });
});

describe('binarySearch', () => {
  it('should return found index', () => {
    expect(binarySearch([1, 2, 3, 4], 4)).toBe(3);
    expect(binarySearch([1, 2, 3, 4, 5, 6, 7], 1)).toBe(0);
    expect(binarySearch([1, 2, 3, 4, 5, 6, 7], 7)).toBe(6);
    expect(binarySearch([1, 2, 3, 4, 5, 6, 7], 4)).toBe(3);
    expect(binarySearch([1, 2, 3, 4, 5, 6], 3)).toBe(2);
  });

  it('should return -1 if not found', () => {
    expect(binarySearch([1, 2, 3], 4)).toBe(-1);
  });
});

describe('naiveStringSearch', () => {
  it('should work', () => {
    expect(
      nativeStringSearch('This is very slow naive string search', 'is')
    ).toBe(2);
  });
});

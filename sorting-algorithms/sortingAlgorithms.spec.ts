import { timeFunc } from '../utils';
import {
  bubbleSort,
  countDigits,
  getDigit,
  getMaxDigit,
  insertionSort,
  mergeSort,
  mergeWhileSorting,
  pivot,
  quickSort,
  radixSort,
  selectionSort,
} from './sortingAlgorithms';

describe('bubbleSort', () => {
  it('works', () => {
    expect(bubbleSort([5, 2, 8, -3, 0, -65])).toEqual([-65, -3, 0, 2, 5, 8]);
  });
  it('works better with almost sorted array', () => {
    const sortedNumbers = [...Array(1000)].map((_, i) => i);
    const reverseSortedNumbers = sortedNumbers.slice().reverse();

    const [sortedDelta, sortedResult] = timeFunc(() =>
      bubbleSort(sortedNumbers)
    );
    const [reverseDelta, reverseResult] = timeFunc(() =>
      bubbleSort(reverseSortedNumbers)
    );

    expect(sortedDelta).toBeLessThan(reverseDelta / 2);
    expect(sortedResult).toEqual(reverseResult);
  });
});

describe('selectionSort', () => {
  it('works', () => {
    expect(selectionSort([5, 2, 8, -3, 0, -65])).toEqual([-65, -3, 0, 2, 5, 8]);
  });
});

describe('insertionSort', () => {
  it('works', () => {
    expect(insertionSort([5, 2, 8, -3, 0, -65])).toEqual([-65, -3, 0, 2, 5, 8]);
  });

  it('should work better when adding new item', () => {
    const reverseSortedNumbers = [...Array(1000)].map((_, i) => 1000 - i);
    const [delta, result] = timeFunc(() => insertionSort(reverseSortedNumbers));
    const newArray = [...result, -100];
    const [newDelta, newResult] = timeFunc(() => insertionSort(newArray));
    expect(newDelta).toBeLessThan(delta / 2);
    expect(newResult).toEqual([-100, ...result]);
  });
});

describe('mergeWhileSorting', () => {
  it('should return a sorted array', () => {
    const arr1 = [1, 4, 7];
    const arr2 = [2, 3, 8, 12];
    expect(mergeWhileSorting(arr1, arr2)).toEqual([1, 2, 3, 4, 7, 8, 12]);
  });

  it('should work with one empty array', () => {
    const arr1 = [] as number[];
    const arr2 = [2, 3, 8, 12];
    expect(mergeWhileSorting(arr1, arr2)).toEqual(arr2);
  });
});

describe('mergeSort', () => {
  it('should work', () => {
    expect(mergeSort([1, 5, 2, 8, -3, 0, -65])).toEqual([
      -65, -3, 0, 1, 2, 5, 8,
    ]);
  });
});

describe('pivot', () => {
  it('should return the correct pivot index', () => {
    const arr = [5, 2, 4, 1, 13, 8];
    const pivotIndex = pivot(arr);
    expect(pivotIndex).toBe(3);
  });
  it('should have smaller values to the left of the pivot', () => {
    const arr = [5, 2, 4, 1, 13, 8];
    const pivotValue = arr[0];
    const pivotIndex = pivot(arr);
    const left = arr.slice(0, pivotIndex);
    expect(left.every((item) => item < pivotValue)).toBe(true);
  });

  it('should have larger values to the right of the pivot', () => {
    const arr = [5, 2, 4, 1, 13, 8];
    const pivotValue = arr[0];
    const pivotIndex = pivot(arr);
    const right = arr.slice(pivotIndex + 1);
    expect(right.every((item) => item > pivotValue)).toBe(true);
  });
});

describe('quickSort', () => {
  it('should sort an array in place', () => {
    const arr = [5, 2, 4, 1, 13, 8];
    quickSort(arr);
    expect(arr).toEqual([1, 2, 4, 5, 8, 13]);
  });
});

describe('getDigit', () => {
  it('returns correct digit', () => {
    expect(getDigit(12345, 0)).toBe(5);
    expect(getDigit(12345, 1)).toBe(4);
    expect(getDigit(12345, 2)).toBe(3);
    expect(getDigit(12345, 3)).toBe(2);
    expect(getDigit(12345, 4)).toBe(1);
  });
  it('returns 0 when place exceeds the digits', () => {
    expect(getDigit(12345, 5)).toBe(0);
  });
  it('works for negative numbers', () => {
    expect(getDigit(-12345, 0)).toBe(5);
  });
});

describe('countDigits', () => {
  it('returns number of digits', () => {
    expect(countDigits(1)).toBe(1);
    expect(countDigits(23)).toBe(2);
    expect(countDigits(456)).toBe(3);
  });
  it('works for negative numbers', () => {
    expect(countDigits(-1234)).toBe(4);
  });
  it('works for 0', () => {
    expect(countDigits(0)).toBe(0);
  });
});

describe('getMaxDigit', () => {
  it('works', () => {
    expect(getMaxDigit([1, 11, 111])).toBe(3);
    expect(getMaxDigit([1, 1, 1])).toBe(1);
    expect(getMaxDigit([4321, 1, 23])).toBe(4);
  });
  it('returns 0 for empty array', () => {
    expect(getMaxDigit([])).toBe(0);
  });
});

describe('radixSort', () => {
  it('works', () => {
    expect(radixSort([1, 5, 2, 8, 3, 0, 65])).toEqual([0, 1, 2, 3, 5, 8, 65]);
    expect(radixSort([111, 15, 22242, 84, 3, 0, 65])).toEqual([
      0, 3, 15, 65, 84, 111, 22242,
    ]);
  });
});

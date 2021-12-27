import { timeFunc } from '../utils';
import {
  bubbleSort,
  insertionSort,
  mergeSort,
  mergeWhileSorting,
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

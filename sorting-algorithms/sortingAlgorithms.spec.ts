import { timeFunc } from '../utils';
import { bubbleSort, insertionSort, selectionSort } from './sortingAlgorithms';

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

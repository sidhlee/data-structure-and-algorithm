import { bubbleSort, selectionSort } from './sortingAlgorithms';

describe('bubbleSort', () => {
  it('works', () => {
    expect(bubbleSort([5, 2, 8, -3, 0, -65])).toEqual([-65, -3, 0, 2, 5, 8]);
  });
  it('works better with almost sorted array', () => {
    const sortedNumbers = [...Array(1000)].map((_, i) => i);
    const reverseSortedNumbers = sortedNumbers.slice().reverse();

    const sortedStart = performance.now();
    const sortedResult = bubbleSort(sortedNumbers);
    const sortedEnd = performance.now();
    const sortedDelta = sortedEnd - sortedStart;

    const reverseStart = performance.now();
    const reverseResult = bubbleSort(reverseSortedNumbers);
    const reverseEnd = performance.now();
    const reverseDelta = reverseEnd - reverseStart;

    expect(sortedDelta).toBeLessThan(reverseDelta / 2);
    expect(sortedResult).toEqual(reverseResult);
  });
});

describe('selectionSort', () => {
  it('works', () => {
    expect(selectionSort([5, 2, 8, -3, 0, -65])).toEqual([-65, -3, 0, 2, 5, 8]);
  });
});

import { bubbleSort } from './sortingAlgorithms';

describe('bubbleSort', () => {
  it('works', () => {
    expect(bubbleSort([5, 2, 8, -3, 0, -65])).toEqual([-65, -3, 0, 2, 5, 8]);
  });
});

import { same } from './frequencyCounterPatternNaive';

describe('same', () => {
  it('returns true if every value in the array has its corresponding value squared in the second array.', () => {
    const result = same([1, 2, 3], [4, 1, 9]);
    expect(result).toBe(true);
  });
});

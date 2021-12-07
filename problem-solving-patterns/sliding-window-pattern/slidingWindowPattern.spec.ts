import {
  maxSubarraySum,
  maxSubarraySumConstantSpace,
} from './slidingWindowPattern';

describe('maxSubarraySum', () => {
  it('finds the max sum of two consecutive numbers', () => {
    const result = maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 2);
    expect(result).toBe(10);
  });
  it('finds the max sum of four consecutive numbers', () => {
    const result = maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 4);
    expect(result).toBe(17);

    const result2 = maxSubarraySum([4, 2, 1, 6, 2], 4);
    expect(result2).toBe(13);
  });
  it('finds the max sum of one number', () => {
    const result = maxSubarraySum([4, 2, 1, 6], 1);
    expect(result).toBe(6);
  });
  it('returns null when given an empty array', () => {
    const result = maxSubarraySum([], 4);
    expect(result).toBe(null);
  });
});

describe('maxSubarraySumConstantSpace', () => {
  it('finds the max sum of two consecutive numbers', () => {
    const result = maxSubarraySumConstantSpace([1, 2, 5, 2, 8, 1, 5], 2);
    expect(result).toBe(10);
  });
  it('finds the max sum of four consecutive numbers', () => {
    const result = maxSubarraySumConstantSpace([1, 2, 5, 2, 8, 1, 5], 4);
    expect(result).toBe(17);

    const result2 = maxSubarraySumConstantSpace([4, 2, 1, 6, 2], 4);
    expect(result2).toBe(13);
  });
  it('finds the max sum of one number', () => {
    const result = maxSubarraySumConstantSpace([4, 2, 1, 6], 1);
    expect(result).toBe(6);
  });
  it('returns null when given an empty array', () => {
    const result = maxSubarraySumConstantSpace([], 4);
    expect(result).toBe(null);
  });
});

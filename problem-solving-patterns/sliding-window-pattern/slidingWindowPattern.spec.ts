import {
  maxSubarraySum,
  maxSubarraySumConstantSpace,
  minSubarrayLen,
  minSubArrayLenAnswer,
} from './slidingWindowPattern';

describe('maxSubarraySum', () => {
  it('finds the max sum of two consecutive numbers', () => {
    const result = maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 2);
    expect(result).toBe(10);

    const result2 = maxSubarraySum([100, 200, 300, 400], 2);
    expect(result2).toBe(700);
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
  it('returns null if n is greater than the array length', () => {
    const result = maxSubarraySum([1, 2], 3);
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

describe('minSubarrayLen', () => {
  it('works when subarray sum equals target', () => {
    const result = minSubarrayLen([2, 3, 1, 2, 4, 3], 7);
    expect(result).toBe(2);
    expect(minSubarrayLen([2, 1, 6, 5, 4], 9)).toBe(2);
    expect(minSubarrayLen([4, 3, 3, 8, 1, 2, 3], 11)).toBe(2);
  });

  it('works when sum is greater than target', () => {
    expect(minSubarrayLen([3, 1, 7, 11, 2, 9, 8, 21, 62, 33, 19], 52)).toBe(1);
  });

  it('works for the same array with different targets', () => {
    expect(minSubarrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 39)).toBe(3);
    expect(minSubarrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 55)).toBe(5);
    expect(minSubarrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 95)).toBe(0);
  });

  it('works when subarray is the given array', () => {
    expect(minSubarrayLen([1, 2, 3], 6)).toBe(3);
  });
});

describe('minSubArrayLenAnswer', () => {
  it('works when subarray sum equals target', () => {
    const result = minSubArrayLenAnswer([2, 3, 1, 2, 4, 3], 7);
    expect(result).toBe(2);
    expect(minSubArrayLenAnswer([2, 1, 6, 5, 4], 9)).toBe(2);
    expect(minSubArrayLenAnswer([4, 3, 3, 8, 1, 2, 3], 11)).toBe(2);
  });

  it('works when sum is greater than target', () => {
    expect(
      minSubArrayLenAnswer([3, 1, 7, 11, 2, 9, 8, 21, 62, 33, 19], 52)
    ).toBe(1);
  });

  it('works for the same array with different targets', () => {
    expect(minSubArrayLenAnswer([1, 4, 16, 22, 5, 7, 8, 9, 10], 39)).toBe(3);
    expect(minSubArrayLenAnswer([1, 4, 16, 22, 5, 7, 8, 9, 10], 55)).toBe(5);
    expect(minSubArrayLenAnswer([1, 4, 16, 22, 5, 7, 8, 9, 10], 95)).toBe(0);
  });

  it('works when subarray is the given array', () => {
    expect(minSubArrayLenAnswer([1, 2, 3], 6)).toBe(3);
  });

  it('should work', () => {
    expect(minSubArrayLenAnswer([3, 5, 1, 1], 7)).toBe(2);
  });

  it('should work 2', () => {
    expect(minSubArrayLenAnswer([8, 8, 8], 7)).toBe(1);
  });
});

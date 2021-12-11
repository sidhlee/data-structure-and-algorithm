import {
  areThereDuplicates,
  areThereDuplicatesWithSet,
  averagePair,
  countUniqueValues,
  countUniqueValuesWithSet,
  isSubsequence,
  sumZero,
  sumZeroNaive,
  sumZeroWithWhileLoop,
} from './multiplePointersPattern';

describe('sumZero', () => {
  it('should find the correct pair', () => {
    const result = sumZero([-3, -2, -1, 0, 1, 2, 3]); // [-3, 3]
    expect(result).toEqual([-3, 3]);
  });

  it('should return undefined when the pair does not exist', () => {
    const result1 = sumZero([-2, 0, 1, 3]);
    expect(result1).toBeUndefined();
    const result2 = sumZero([1, 2, 3]);
    expect(result2).toBeUndefined();
  });
});

describe('sumZeroNaive', () => {
  it('should find the correct pair', () => {
    const result = sumZeroNaive([-3, -2, -1, 0, 1, 2, 3]); // [-3, 3]
    expect(result).toEqual([-3, 3]);
  });

  it('should return undefined when the pair does not exist', () => {
    const result1 = sumZeroNaive([-2, 0, 1, 3]);
    expect(result1).toBeUndefined();
    const result2 = sumZeroNaive([1, 2, 3]);
    expect(result2).toBeUndefined();
  });
});

describe('sumZeroWithWhileLoop', () => {
  it('should find the correct pair', () => {
    const result = sumZeroWithWhileLoop([-3, -2, -1, 0, 1, 2, 3]); // [-3, 3]
    expect(result).toEqual([-3, 3]);
  });

  it('should return undefined when the pair does not exist', () => {
    const result1 = sumZeroWithWhileLoop([-2, 0, 1, 3]);
    expect(result1).toBeUndefined();
    const result2 = sumZeroWithWhileLoop([1, 2, 3]);
    expect(result2).toBeUndefined();
  });
});

describe('countUniqueValues', () => {
  it('should count the unique values', () => {
    const result1 = countUniqueValues([1, 1, 1, 1, 1, 2]);
    expect(result1).toBe(2);

    const result2 = countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]);
    expect(result2).toBe(7);

    const result3 = countUniqueValues([-2, -1, -1, 0, 1]);
    expect(result3).toBe(4);
  });

  it('should return 0 for an empty array', () => {
    const result = countUniqueValues([]);
    expect(result).toBe(0);
  });
});

describe('countUniqueValuesWithSet', () => {
  it('should count the unique values', () => {
    const result1 = countUniqueValuesWithSet([1, 1, 1, 1, 1, 2]);
    expect(result1).toBe(2);

    const result2 = countUniqueValuesWithSet([
      1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13,
    ]);
    expect(result2).toBe(7);

    const result3 = countUniqueValuesWithSet([-2, -1, -1, 0, 1]);
    expect(result3).toBe(4);
  });

  it('should return 0 for an empty array', () => {
    const result = countUniqueValuesWithSet([]);
    expect(result).toBe(0);
  });
});

describe('areThereDuplicates', () => {
  it('should return false if there are no duplicated numbers', () => {
    const result = areThereDuplicates(1, 2, 3);
    expect(result).toBe(false);
  });

  it('should return true if there are any duplicated numbers', () => {
    const result = areThereDuplicates(1, 2, 2);
    expect(result).toBe(true);
  });

  it('should return true if there are any duplicated strings', () => {
    const result = areThereDuplicates('a', 'b', 'c', 'a');
    expect(result).toBe(true);
  });
});

describe('areThereDuplicatesWithSet', () => {
  it('should return false if there are no duplicated numbers', () => {
    const result = areThereDuplicatesWithSet(1, 2, 3);
    expect(result).toBe(false);
  });

  it('should return true if there are any duplicated numbers', () => {
    const result = areThereDuplicatesWithSet(1, 2, 2);
    expect(result).toBe(true);
  });

  it('should return true if there are any duplicated strings', () => {
    const result = areThereDuplicatesWithSet('a', 'b', 'c', 'a');
    expect(result).toBe(true);
  });
});

describe('averagePair', () => {
  it('returns true for non-integer target if the pair is found', () => {
    const result = averagePair([1, 2, 3], 2.5);
    expect(result).toBe(true);
  });
  it('returns true for integer target if hte pair is found', () => {
    const result = averagePair([1, 3, 3, 5, 6, 7, 10, 12, 19], 8);
    expect(result).toBe(true);
  });
  it('returns false if the pair is not found', () => {
    const result = averagePair([-1, 0, 3, 4, 5, 6], 4.1);
    expect(result).toBe(false);
  });
  it('returns false when given an empty array', () => {
    const result = averagePair([], 4);
    expect(result).toBe(false);
  });
});

describe('isSubsequence', () => {
  it('should return true if str1 is found in str2', () => {
    const result = isSubsequence('hello', 'hello world');
    expect(result).toBe(true);
  });

  it('should return true if str1 in found in str2 with a character inserted', () => {
    const result = isSubsequence('sing', 'sting');
    expect(result).toBe(true);
  });

  it('should return true if str1 is found in str2 with many characters inserted', () => {
    const result = isSubsequence('abc', 'abracadabra');
    expect(result).toBe(true);
  });

  it('should return false if the character order is changed', () => {
    const result = isSubsequence('abc', 'acb');
    expect(result).toBe(false);
  });
});

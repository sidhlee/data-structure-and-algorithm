import {
  areThereDuplicates,
  areThereDuplicatesWithSet,
  countUniqueValues,
  countUniqueValuesWithSet,
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

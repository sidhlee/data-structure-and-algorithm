import {
  same,
  sameNaive,
  isAnagram,
  sameFrequency,
  areThereDuplicates,
} from './frequencyCounterPattern';

describe('same', () => {
  it('returns true if every value in the array has its corresponding value squared in the second array.', () => {
    const result = same([1, 2, 3], [4, 1, 9]);
    expect(result).toBe(true);
  });

  it(`returns false if the number of items don't match`, () => {
    const result = same([1, 2, 3], [1, 9]);
    expect(result).toBe(false);
  });

  it(`returns false if the frequency of the number doesn't match`, () => {
    const result = same([1, 2, 1], [4, 4, 1]);
    expect(result).toBe(false);
  });
});

describe('sameNaive', () => {
  it('returns true if every value in the array has its corresponding value squared in the second array.', () => {
    const result = sameNaive([1, 2, 3], [4, 1, 9]);
    expect(result).toBe(true);
  });

  it(`returns false if the number of items don't match`, () => {
    const result = sameNaive([1, 2, 3], [1, 9]);
    expect(result).toBe(false);
  });

  it(`returns false if the frequency of the number doesn't match`, () => {
    const result = sameNaive([1, 2, 1], [4, 4, 1]);
    expect(result).toBe(false);
  });
});

describe('isAnagram', () => {
  it('returns true given two empty strings', () => {
    const result = isAnagram('', '');
    expect(result).toBe(true);
  });

  it('returns false when the frequency of a character differs', () => {
    const result = isAnagram('aaz', 'zza');
    expect(result).toBe(false);
  });

  it('returns true if only the order of the characters are different', () => {
    const result = isAnagram('anagram', 'nagaram');
    expect(result).toBe(true);

    const result2 = isAnagram('qwerty', 'qeyrwt');
    expect(result2).toBe(true);

    const result3 = isAnagram('texttwisttime', 'timetwisttext');
    expect(result3).toBe(true);
  });

  it('returns false when the strings of the same size have different characters', () => {
    const result = isAnagram('rat', 'car');
    expect(result).toBe(false);
  });

  it('returns false if the same set of characters have different frequency', () => {
    const result = isAnagram('awesome', 'awesom');
    expect(result).toBe(false);
  });
});

describe('sameFrequency', () => {
  it('should return true if numbers have the same frequency', () => {
    const result = sameFrequency(182, 281);
    expect(result).toBe(true);
  });
  it('should return false if numbers do not have the same frequency', () => {
    const result = sameFrequency(34, 14);
    expect(result).toBe(false);
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

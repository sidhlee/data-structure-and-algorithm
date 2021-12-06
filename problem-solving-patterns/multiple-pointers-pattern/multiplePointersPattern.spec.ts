import {
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

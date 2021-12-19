import { collectOddValues, collectOddValuesPure } from './recursion';

describe('collectOddValues', () => {
  it('works', () => {
    expect(collectOddValues([1, 2, 3, 4, 5])).toEqual([1, 3, 5]);
  });
});

describe('collectOddValuesPure', () => {
  it('works', () => {
    expect(collectOddValuesPure([1, 2, 3, 4, 5])).toEqual([1, 3, 5]);
  });
});

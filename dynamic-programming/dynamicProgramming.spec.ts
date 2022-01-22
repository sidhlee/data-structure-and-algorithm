import { timeFunc } from '../utils';
import { fib, fibMemo, fibTabulation } from './dynamicProgramming';

describe('fibMemo', () => {
  it('should work', () => {
    expect(fibMemo(4)).toBe(3);
    expect(fibMemo(10)).toBe(55);
    expect(fibMemo(28)).toBe(317811);
    expect(fibMemo(35)).toBe(9227465);
  });

  it('should run much faster than non dynamic solution', () => {
    const [naiveTime] = timeFunc(() => fib(35));
    const [memoTime] = timeFunc(() => fibMemo(35));
    expect(naiveTime).toBeGreaterThan(memoTime * 100);
  });
});

describe('fibTabulation', () => {
  it('should work', () => {
    expect(fibTabulation(4)).toBe(3);
    expect(fibTabulation(10)).toBe(55);
    expect(fibTabulation(28)).toBe(317811);
    expect(fibTabulation(35)).toBe(9227465);
  });

  it('should run much faster than non dynamic solution', () => {
    const [naiveTime] = timeFunc(() => fib(35));
    const [memoTime] = timeFunc(() => fibTabulation(35));
    expect(naiveTime).toBeGreaterThan(memoTime * 100);
  });
});

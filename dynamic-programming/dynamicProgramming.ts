// copied from recursion section for easy comparison.
export function fib(num: number): number {
  if (num < 3) return 1;
  return fib(num - 1) + fib(num - 2);
}

export function fibMemo(num: number, memo = [0, 1, 1]): number {
  if (memo[num]) return memo[num];
  const result = fibMemo(num - 1, memo) + fibMemo(num - 2, memo);
  memo[num] = result;
  return result;
}

export function fibTabulation(num: number) {
  const fibs = [0, 1, 1];
  if (num < 3) return fibs[num];
  for (let i = 3; i <= num; i++) {
    fibs[i] = fibs[i - 1] + fibs[i - 2];
  }
  return fibs[num];
}

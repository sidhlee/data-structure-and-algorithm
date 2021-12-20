// Helper method recursion
export function collectOddValues(arr: number[]) {
  let result = [] as number[];

  function helper(helperInput: number[]) {
    if (helperInput.length === 0) return;
    const isOdd = helperInput[0] % 2 !== 0;
    if (isOdd) {
      result.push(helperInput[0]);
    }
    helper(helperInput.slice(1));
  }
  helper(arr);

  return result;
}

// Pure recursion
export function collectOddValuesPure(arr: number[]): number[] {
  let newArr = [] as number[];
  if (arr.length === 0) return newArr;
  const isOdd = arr[0] % 2 !== 0;
  if (isOdd) {
    newArr.push(arr[0]);
  }
  return newArr.concat(collectOddValuesPure(arr.slice(1)));
}

/**
 * Should return the power of the base to the exponent. Assume that the base and the exponent is greater than or equal to 0.
 * @param base
 * @param exponent
 */
export function power(base: number, exponent: number): number {
  if (exponent === 0) return 1;
  return base * power(base, exponent - 1);
}

/**
 * Returns the factorial of the given number. Factorial of 0 is always 1.
 */
export function factorial(num: number): number {
  if (num < 0) throw Error('cannot take factorial of negative number.');
  if (num === 0) return 1;
  return num * factorial(num - 1);
}

export function productOfArray(numbers: number[]): number {
  if (numbers.length === 0) throw Error('array must have at least one number');
  if (numbers.length === 1) return numbers[0];
  return numbers[0] * productOfArray(numbers.slice(1));
}

/**
 * Adds up all the numbers from 0 to the given number.
 * @param num positive integer
 */
export function sumRange(num: number): number {
  if (num === 1) return 1;
  return num + sumRange(num - 1);
}

/**
 * Returns nth number of fibonacci sequence eg. 1, 1, 2, 3, 5,...
 * @param num positive integer
 */
export function fib(num: number): number {
  if (num < 3) return 1;
  return fib(num - 1) + fib(num - 2);
}

// 1, 1, 2, 3, 5, 8, 11
// 1  2  3  4  5  6  7

export function reverse(str: string): string {
  if (str.length === 1) return str;
  return str[str.length - 1] + reverse(str.slice(0, -1));
}

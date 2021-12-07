// O(n) time but with O(n) space
export function maxSubarraySum(numbers: number[], n: number) {
  if (numbers.length === 0) return null;

  let max = -Infinity;
  for (let i = 0; i < numbers.length - n + 1; i++) {
    const subarray = numbers.slice(i, i + n);
    const sum = sumArray(subarray);
    if (sum > max) {
      max = sum;
    }
  }
  return max;
}

function sumArray(numbers: number[]) {
  return numbers.reduce((acc, val) => acc + val);
}

export function maxSubarraySumConstantSpace(numbers: number[], n: number) {
  if (numbers.length < n) return null;
  let currentSum = 0;

  // loop once to sum initial window
  for (let i = 0; i < n; i++) {
    currentSum += numbers[i];
  }
  let max = currentSum;

  for (let i = n; i < numbers.length; i++) {
    // slide the window
    const oldFirst = numbers[i - n];
    const newNumber = numbers[i];
    currentSum = currentSum - oldFirst + newNumber;

    if (currentSum > max) {
      max = currentSum;
    }
    // could also use max = Math.max(max, currentSum)
  }
  return max;
}

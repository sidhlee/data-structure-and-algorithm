// O(n) time but with O(n) space
export function maxSubarraySum(numbers: number[], n: number) {
  if (numbers.length < n) return null;

  let max = -Infinity;

  const lastSubarrayStartIndex = numbers.length - n;

  for (let i = 0; i <= lastSubarrayStartIndex; i++) {
    const subarray = numbers.slice(i, i + n);
    const sum = sumArray(subarray);
    if (sum > max) {
      max = sum;
    }
  }
  return max;
}

//  0, 1, 2, 3, 4 (index)
// [1, 2, 3, 4, 5], n = 3
//

function sumArray(numbers: number[]) {
  return numbers.reduce((acc, val) => acc + val);
}

export function maxSubarraySumConstantSpace(
  numbers: number[],
  subarraySize: number
) {
  if (numbers.length < subarraySize) return null;
  let currentSum = 0;

  // loop once to sum initial window
  for (let i = 0; i < subarraySize; i++) {
    currentSum += numbers[i];
  }
  let max = currentSum;

  for (let i = 1; i < numbers.length; i++) {
    // slide the window
    const removedNumber = numbers[i - 1];
    const addedNumber = numbers[i + subarraySize - 1];
    currentSum = currentSum - removedNumber + addedNumber;

    if (currentSum > max) {
      max = currentSum;
    }
    // could also use max = Math.max(max, currentSum)
  }
  return max;
}

export function minSubarrayLen(arr: number[], minSum: number) {
  let subarrayLength = 1;
  let largestNumberIndex = 0;
  // Find the max value to decide where to grow subarray from
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > arr[largestNumberIndex]) {
      largestNumberIndex = i;
    }
  }
  // Loop only until subarraySum is smaller than min sum and also,
  // subarray length is smaller than array length
  let subarraySum = arr[largestNumberIndex];
  let subarrayHeadIndex = largestNumberIndex;
  let subarrayTailIndex = largestNumberIndex;
  while (subarraySum < minSum && subarrayLength < arr.length) {
    if (shouldGrowLeft(arr, subarrayHeadIndex, subarrayTailIndex)) {
      subarrayHeadIndex--;
      subarraySum += arr[subarrayHeadIndex];
    } else {
      subarrayTailIndex++;
      subarraySum += arr[subarrayTailIndex];
    }
    subarrayLength++;
  }
  if (subarraySum >= minSum) return subarrayLength;
  return 0;
}

function shouldGrowLeft(
  arr: number[],
  subarrayHeadIndex: number,
  subarrayTailIndex: number
) {
  // handle edge cases
  if (subarrayHeadIndex === 0 && subarrayTailIndex === arr.length - 1)
    throw Error('Subarray cannot grow anymore');
  if (subarrayHeadIndex === 0) return false;
  if (subarrayTailIndex === arr.length - 1) return true;
  // look backward and ahead to decide in which direction subarray should grow
  const beforeValue = arr[subarrayHeadIndex - 1];
  const afterValue = arr[subarrayTailIndex + 1];
  if (beforeValue > afterValue) return true;

  return false;
}

export function minSubArrayLenAnswer(numbers: number[], minSum: number) {
  let sum = 0;
  let headIndex = 0;
  let tailIndex = 0;
  let minLen = Infinity;

  while (headIndex < numbers.length) {
    // Update sum and move the tail if sum < minSum and tail is in range
    if (sum < minSum && tailIndex < numbers.length) {
      // when tail reached the end, last value will be added to sum,
      // and the tail is pushed out of the numbers array
      sum += numbers[tailIndex];
      tailIndex++;
    }
    // If the sum became geq to minSum && currentWindowLength < minLen, update minLen
    // Also move the head resetting the window and current sum
    else if (sum >= minSum) {
      // take one off since tail was moved after getting the sum
      const currentWindowLength = tailIndex - headIndex + 1 - 1;
      minLen = Math.min(minLen, currentWindowLength);

      sum -= numbers[headIndex];
      headIndex++;
    }
    // Tail is moved out of the array
    else {
      break;
    }
  }
  // Tail or Head is moved out of the array
  return minLen === Infinity ? 0 : minLen;
}

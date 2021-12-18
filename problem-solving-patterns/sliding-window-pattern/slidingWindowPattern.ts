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

export function findLongestSubstring(str: string) {
  if (str.length <= 1) return str.length;
  // str.length >= 2
  let maxLen = 1;
  let headIndex = 0;
  let tailIndex = 1;
  const headValue = str[headIndex];
  let chars = { [headValue]: headIndex };
  // loop while indices are within the range
  while (headIndex < str.length && tailIndex < str.length) {
    const tailValue = str[tailIndex];
    // tail value is unique WITHIN the window
    const isTailValueUnique =
      chars[tailValue] === undefined || chars[tailValue] < headIndex;
    if (isTailValueUnique) {
      // register the new unique value and save its index
      chars[tailValue] = tailIndex;
    } else {
      // set the head right after the old existing char
      headIndex = chars[tailValue] + 1;
      // update the char index with the index of the duplicated value
      // so that we can keep the index within the window
      chars[tailValue] = tailIndex;
    }
    // update the max length with the current head & tail index
    maxLen = Math.max(maxLen, tailIndex - headIndex + 1);

    tailIndex++;
  }
  return maxLen;
}
// "abcbac"
//    h
//     t

// bbb
// h
//  t

export function findLongestSubstringWithForLoop(str: string) {
  let longest = 0;
  let headIndex = 0;
  const seen = {} as { [char: string]: number };
  // Find all substring with non-repeating characters and keep records of the longest
  for (let tailIndex = 0; tailIndex < str.length; tailIndex++) {
    const tailValue = str[tailIndex];
    const lastSeenIndex = seen[tailValue];
    if (lastSeenIndex !== undefined) {
      // headIndex can't go back
      headIndex = Math.max(lastSeenIndex + 1, headIndex);
    }
    seen[tailValue] = tailIndex;
    const newSubstringLength = tailIndex - headIndex + 1;
    longest = Math.max(longest, newSubstringLength);
  }
  return longest;
}

// thecatinthehat
//       h
//          t

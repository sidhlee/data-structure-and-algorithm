/**
import { areThereDuplicates } from '../frequency-counter-pattern/frequencyCounterPattern';
 * Space: O(1), Time: O(n)
 */
export function sumZero(sortedArray: number[]) {
  // create pointers
  let headIndex = 0;
  let tailIndex = sortedArray.length - 1;
  // loop until before pointers meet
  for (let i = 0; i < Math.floor(sortedArray.length / 2); i++) {
    const sum = sortedArray[headIndex] + sortedArray[tailIndex];
    if (sum > 0) {
      // sum is positive -> tail value is too big eg. [-2, 3]
      tailIndex--;
    } else if (sum < 0) {
      // sum is negative -> head value is too small eg. [-3, 2]
      headIndex++;
    } else {
      // sum is 0
      return [sortedArray[headIndex], sortedArray[tailIndex]];
    }
  }

  return undefined;
}

/**
 * Space: O(1), Time: O(n^2)
 * Not taking advantage of the assumption
 */
export function sumZeroNaive(unsortedArray: number[]) {
  for (let i = 0; i < unsortedArray.length; i++) {
    for (let j = 1; j < unsortedArray.length; j++) {
      const firstValue = unsortedArray[i];
      const secondValue = unsortedArray[j];
      const sum = firstValue + secondValue;
      // should not return [0, 0] when i and j are the same
      if (sum === 0 && i !== j) return [firstValue, secondValue];
    }
  }
  return undefined;
}

/**
 * Space: O(1), Time: O(n).
 * While loop is great when you need to loop until x condition.
 */
export function sumZeroWithWhileLoop(sortedArray: number[]) {
  // create pointers
  let headIndex = 0;
  let tailIndex = sortedArray.length - 1;
  // loop until before pointers meet
  while (headIndex < tailIndex) {
    const sum = sortedArray[headIndex] + sortedArray[tailIndex];
    if (sum === 0) {
      // check if we got what we want first. don't need wait for moving pointers
      // ie. shoot first
      return [sortedArray[headIndex], sortedArray[tailIndex]];
    } else if (sum > 0) {
      // move counter if we don't see what we're looking for
      // like adjusting the aim after missing the target
      // sum is positive -> tail value is too big eg. [-2, 3]
      tailIndex--;
    } else {
      // sum is negative -> head value is too small eg. [-3, 2]
      headIndex++;
    }
  }

  return undefined;
}

export function countUniqueValues(sortedArray: number[]) {
  if (sortedArray.length === 0) return 0;
  let leftIndex = 0;
  let rightIndex = 1;
  let count = 1;
  // if sortedArray is mutated while looping, this can break
  while (rightIndex < sortedArray.length) {
    const leftValue = sortedArray[leftIndex];
    const rightValue = sortedArray[rightIndex];
    if (leftValue === rightValue) {
      rightIndex++;
    } else {
      count++;
      rightIndex++;
      leftIndex = rightIndex - 1;
    }
  }
  return count;
}

export function countUniqueValuesWithSet(sortedArray: number[]) {
  const set = new Set(sortedArray);
  return set.size;
}

type Arg = string | number;
export function areThereDuplicates(...args: Arg[]) {
  let leftIndex = 0;
  let rightIndex = 1;
  const sortedArgs = args.sort();
  while (rightIndex < args.length) {
    const leftValue = sortedArgs[leftIndex];
    const rightValue = sortedArgs[rightIndex];
    if (leftValue === rightValue) return true;
    leftIndex++;
    rightIndex++;
  }
  return false;
}

export function areThereDuplicatesWithSet(...args: Arg[]) {
  return new Set(args).size !== args.length;
}

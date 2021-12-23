export function linearSearch(arr: any[], target: any) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) return i;
  }
  return -1;
}

export function binarySearch<T>(arr: T[], target: T) {
  let headIndex = 0;
  let tailIndex = arr.length - 1;
  while (headIndex <= tailIndex) {
    const midIndex = Math.floor((headIndex + tailIndex) / 2);
    const midValue = arr[midIndex];
    if (midValue === target) {
      return midIndex;
    } else if (target > midValue) {
      headIndex = midIndex + 1;
    } else {
      tailIndex = midIndex - 1;
    }
  }
  return -1;
}

// [1, 2, 3, 4]
//     m

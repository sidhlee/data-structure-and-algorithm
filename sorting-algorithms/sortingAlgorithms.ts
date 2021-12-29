export function bubbleSort(arr: number[]) {
  const copy = arr.slice();
  for (let i = copy.length - 1; i > 0; i--) {
    let haveSwapped = false;
    for (let j = 0; j < i; j++) {
      const curr = copy[j];
      const next = copy[j + 1];
      if (curr > next) {
        swap(copy, j, j + 1);
        haveSwapped = true;
      }
    }
    // Optimization
    if (!haveSwapped) {
      // array already sorted
      break;
    }
  }
  return copy;
}

/**
 * swaps items in the array in place.
 * @param arr
 * @param index1
 * @param index2
 */
function swap(arr: any[], index1: number, index2: number) {
  const temp = arr[index1];
  arr[index1] = arr[index2];
  arr[index2] = temp;
}

export function selectionSort(arr: number[]) {
  const copy = arr.slice();
  for (let i = 0; i < copy.length - 1; i++) {
    let minIndex = i;
    for (let j = i + 1; j < copy.length; j++) {
      if (copy[j] < copy[minIndex]) minIndex = j;
    }
    if (copy[i] !== copy[minIndex]) swap(copy, i, minIndex);
  }
  return copy;
}

export function insertionSort(arr: number[]) {
  if (arr.length === 0) return arr;
  const copy = arr.slice();
  for (let i = 1; i < copy.length; i++) {
    const newItem = arr[i];
    let j;
    for (j = i - 1; j >= 0; j--) {
      if (copy[j] <= newItem) {
        break;
      } else {
        // if new item is smaller than current item, copy the current item to the right
        copy[j + 1] = copy[j];
      }
    }
    // if the new item is geq to the last subarray item, don't bother to insert
    if (j === i - 1) continue;
    // insert to the right of the subarray value that was smaller than the new item
    copy[j + 1] = newItem;
  }
  return copy;
}

export function mergeWhileSorting(arr1: number[], arr2: number[]) {
  const result = [] as number[];
  let i = 0;
  let j = 0;
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      result.push(arr1[i]);
      i++;
    } else {
      result.push(arr2[j]);
      j++;
    }
  }
  while (i < arr1.length) {
    result.push(arr1[i]);
    i++;
  }
  while (j < arr2.length) {
    result.push(arr2[j]);
    j++;
  }

  return result;
}

export function mergeSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;
  const middle = Math.floor(arr.length / 2);
  const arr1 = arr.slice(0, middle);
  const arr2 = arr.slice(middle);

  return mergeWhileSorting(mergeSort(arr1), mergeSort(arr2));
}

export function pivot(
  arr: number[],
  headIndex = 0,
  tailIndex = arr.length - 1
) {
  let pivotIndex = headIndex;
  const pivotValue = arr[pivotIndex];
  for (let i = pivotIndex + 1; i <= tailIndex; i++) {
    // place any value smaller than pivot to the current pivotIndex + 1
    // then advance the pivot index
    if (pivotValue > arr[i]) {
      // swapping smaller value with the value next to the pivot index
      // so that we can keep the pivot value at the beginning of the array
      // and later move it to the pivot index
      swap(arr, i, pivotIndex + 1);
      // we don't need to add 1 if we increment the pivot index first
      // but this makes it easier for me to understand.
      pivotIndex++;
    }
  }
  // move to pivot to the pivot index to sit between smaller and larger items
  // arr[pivotIndex] = pivotValue;
  swap(arr, pivotIndex, headIndex);
  return pivotIndex;
}

export function quickSort(
  arr: number[],
  headIndex = 0,
  tailIndex = arr.length - 1
) {
  if (headIndex < tailIndex) {
    const pivotIndex = pivot(arr, headIndex, tailIndex);
    quickSort(arr, headIndex, pivotIndex - 1);
    quickSort(arr, pivotIndex + 1, tailIndex);
  }
  return arr;
}

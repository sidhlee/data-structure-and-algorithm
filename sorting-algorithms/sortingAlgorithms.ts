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

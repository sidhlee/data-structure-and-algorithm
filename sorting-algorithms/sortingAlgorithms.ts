export function bubbleSort(arr: number[]) {
  const copy = arr.slice();
  for (let i = copy.length - 1; i > 0; i--) {
    for (let j = 0; j < i; j++) {
      const curr = copy[j];
      const next = copy[j + 1];
      if (curr > next) {
        swap(copy, j, j + 1);
      }
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

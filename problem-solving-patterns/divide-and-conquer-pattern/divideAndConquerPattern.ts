export function binarySearch(sortedArray: number[], value: number) {
  let head = 0;
  let tail = sortedArray.length - 1;
  let middle = Math.floor(sortedArray.length / 2);

  while (head <= tail) {
    const middleValue = sortedArray[middle];
    if (value < middleValue) {
      tail = middle - 1;
      middle = getMiddle(head, tail);
    } else if (value > middleValue) {
      head = middle + 1;
      middle = getMiddle(head, tail);
    } else {
      // divider value equals to the value
      return middle;
    }
  }
  return -1;
}

function getMiddle(head: number, tail: number) {
  return Math.floor((head + tail) / 2);
}
// 0, 1, 2, 3, 4, 5: index
// 1, 2, 3, 4, 5, 6: value
//               htm
//                n

export class MaxBinaryHeap {
  values: number[];
  constructor() {
    this.values = [];
  }

  insert(value: number) {
    this.values.push(value);
    this.bubbleUp();

    return this;
  }

  extractMax() {
    this.swap(this.values, 0, this.values.length - 1);
    const max = this.values.pop();
    this.bubbleDown();
    return max;
  }

  private bubbleUp() {
    let insertedValueIndex = this.values.length - 1;
    const insertedValue = this.values[insertedValueIndex];
    let parentIndex = this.getParentIndex(insertedValueIndex);
    if (parentIndex === -1) return; // no parent node, stop.

    while (true) {
      const parentValue = this.values[parentIndex];
      if (insertedValue >= parentValue) {
        this.swap(this.values, insertedValueIndex, parentIndex);
      } else {
        return;
      }
      // update indices before next iteration
      insertedValueIndex = parentIndex;
      parentIndex = this.getParentIndex(insertedValueIndex);
    }
  }

  private bubbleDown() {
    let rootIndex = 0;
    let leftIndex = 1;
    let rightIndex = 2;
    while (true) {
      const rootValue = this.values[rootIndex];
      const maxChildIndex = this.getMaxIndex(leftIndex, rightIndex);
      // break if there are no children
      if (maxChildIndex === undefined) break;
      const maxChildValue = this.values[maxChildIndex];

      if (maxChildValue > rootValue) {
        this.swap(this.values, rootIndex, maxChildIndex);
      } else {
        // break if children value is less than or equal to the bubble
        break;
      }
      rootIndex = maxChildIndex;
      leftIndex = this.getLeftIndex(rootIndex);
      rightIndex = this.getRightIndex(rootIndex);
    }
  }

  private getMaxIndex(leftIndex: number, rightIndex: number) {
    const isLeftIndexValid = leftIndex >= 0 && leftIndex < this.values.length;
    const isRightIndexValid =
      rightIndex >= 0 &&
      rightIndex < this.values.length &&
      leftIndex < rightIndex;
    const leftValue = this.values[leftIndex];
    const rightValue = this.values[rightIndex];
    if (isLeftIndexValid && isRightIndexValid) {
      // comparison operator returns false if either side gets undefined
      return leftValue > rightValue ? leftIndex : rightIndex;
    } else if (isLeftIndexValid && !isRightIndexValid) {
      return leftIndex;
    } else {
      // BinaryHeap cannot have rightChild without leftChild
      return undefined;
    }
  }

  private getParentIndex(childIndex: number) {
    return Math.floor((childIndex - 1) / 2);
  }

  /**
   * swaps two items in the given array in place.
   * @param arr
   * @param index1
   * @param index2
   * @returns
   */
  private swap(arr: any[], index1: number, index2: number) {
    const item1 = arr[index1];
    const item2 = arr[index2];
    arr[index1] = item2;
    arr[index2] = item1;
    return arr;
  }

  private getLeftIndex(parentIndex: number) {
    return 2 * parentIndex + 1;
  }

  private getRightIndex(parentIndex: number) {
    return 2 * parentIndex + 2;
  }
}

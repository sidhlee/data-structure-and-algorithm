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
}

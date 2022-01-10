export class Node {
  constructor(public value: any, public priority: number) {}
}

/**
 * Priority Queue implemented with min binary heap.
 * Lower number means higher priority.
 */
export class PriorityQueue {
  nodes: Node[];
  constructor() {
    this.nodes = [];
  }

  /**
   * create a node and place it at the correct position based on priority
   * @param value
   * @param priority
   */
  enqueue(value: any, priority: number) {
    const newNode = new Node(value, priority);
    this.nodes.push(newNode);
    if (this.nodes.length > 1) {
      this.bubbleUp();
    }
  }

  /**
   * Removes root and returns it after rearranging the heap
   */
  dequeue() {
    this.swap(0, this.nodes.length - 1);
    const minNode = this.nodes.pop();
    this.bubbleDown();
    return minNode;
  }

  private bubbleUp() {
    let newNodeIndex = this.nodes.length - 1;
    while (newNodeIndex > 0) {
      const newNodePriority = this.nodes[newNodeIndex].priority;
      const parentNodeIndex = this.getParentNodeIndex(newNodeIndex);
      const parentNodePriority = this.nodes[parentNodeIndex].priority;

      if (newNodePriority >= parentNodePriority) break;

      this.swap(newNodeIndex, parentNodeIndex);
      newNodeIndex = parentNodeIndex;
    }
  }

  private bubbleDown() {
    let bubblingNodeIndex = 0;
    while (bubblingNodeIndex < this.nodes.length) {
      const smallerChildIndex = this.getSmallerChildIndex(bubblingNodeIndex);
      // break if no children
      if (!smallerChildIndex) break;
      this.swap(bubblingNodeIndex, smallerChildIndex);
      bubblingNodeIndex = smallerChildIndex;
    }
  }

  private getParentNodeIndex(childIndex: number) {
    return Math.floor((childIndex - 1) / 2);
  }

  private getSmallerChildIndex(bubblingNodeIndex: number) {
    const leftChildIndex = bubblingNodeIndex * 2 + 1;
    const rightChildIndex = bubblingNodeIndex * 2 + 2;
    const leftChildIndexValid =
      leftChildIndex >= 0 && leftChildIndex < this.nodes.length;
    const rightChildIndexValid =
      rightChildIndex >= 0 && rightChildIndex < this.nodes.length;
    if (leftChildIndexValid && !rightChildIndexValid) {
      return leftChildIndex;
    } else if (!leftChildIndexValid && rightChildIndexValid) {
      return rightChildIndex;
    } else if (leftChildIndexValid && rightChildIndexValid) {
      const leftChildNode = this.nodes[leftChildIndex];
      const rightChildNode = this.nodes[rightChildIndex];
      return leftChildNode.priority < rightChildNode.priority
        ? leftChildIndex
        : rightChildIndex;
      return;
    } else {
      return undefined;
    }
  }

  private swap(indexA: number, indexB: number) {
    const tempA = this.nodes[indexA];
    this.nodes[indexA] = this.nodes[indexB];
    this.nodes[indexB] = tempA;
  }
}

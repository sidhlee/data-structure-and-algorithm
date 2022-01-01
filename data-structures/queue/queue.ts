export class Node<T> {
  next: Node<T> | null;
  constructor(public value: T) {
    this.next = null;
  }
}

export class Queue<T> {
  first: Node<T> | null;
  last: Node<T> | null;
  size: number;
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  enqueue(value: T) {
    const newNode = new Node(value);
    if (!this.first || !this.last) {
      this.first = newNode;
      this.last = newNode;
    } else {
      const oldLast = this.last;
      this.last = newNode;
      oldLast.next = this.last;
    }
    this.size++;
    return this.size;
  }
  dequeue() {
    if (!this.first || !this.last) return null;
    const dequeuedNode = this.first;
    // there is only one value;
    if (this.first === this.last) {
      this.first = null;
      this.last = null;
    } else {
      this.first = dequeuedNode.next;
    }
    this.size--;
    return dequeuedNode.value;
  }
}

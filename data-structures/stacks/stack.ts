export class Node<T> {
  next: Node<T> | null;
  constructor(public value: T) {
    this.value = value;
    this.next = null;
  }
}

export class Stack<T> {
  first: Node<T> | null;
  last: Node<T> | null;
  size: number;
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  push(value: T) {
    const newNode = new Node(value);
    if (!this.first || !this.last) {
      this.first = newNode;
      this.last = newNode;
    } else {
      const oldLast = this.last;
      oldLast.next = newNode;
      this.last = newNode;
    }
    this.size++;
    return this.size;
  }

  pop() {
    if (!this.first || !this.last) return null;
    const poppedNode = this.first;
    if (this.size < 2) {
      this.first = null;
      this.last = null;
    } else {
      this.first = this.first.next;
    }
    this.size--;
    return poppedNode.value;
  }
}

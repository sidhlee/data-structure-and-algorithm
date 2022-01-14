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
      // setting new node as first to be able to pop with O(1)
      const oldFirst = this.first;
      this.first = newNode;
      this.first.next = oldFirst;
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
      // if we're using last to pop, it would take O(n) to find the second last and update it to be the last
      this.first = this.first.next;
    }
    this.size--;
    return poppedNode.value;
  }
}

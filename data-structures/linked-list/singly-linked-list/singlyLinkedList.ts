import Node from './node';

export default class SinglyLinkedList<T> {
  constructor(
    public head: Node<T> | null = null,
    public tail: Node<T> | null = null,
    public length: number = 0
  ) {}

  public push(val: T) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
    }
    if (this.tail) {
      this.tail.next = newNode;
    }
    this.tail = newNode;
    this.length++;
    return this;
  }
}

import Node from './node';

export default class SinglyLinkedList<T> {
  constructor(
    public head: Node<T> | null = null,
    public tail: Node<T> | null = null,
    public length: number = 0
  ) {}

  public push(val: T) {
    const newNode = new Node(val);
    if (!this.tail) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }

  public pop() {
    if (!this.head) return undefined;
    let currentNode = this.head;
    let newTail = currentNode;
    while (currentNode.next) {
      newTail = currentNode;
      currentNode = currentNode.next;
    }
    this.tail = newTail;
    newTail.next = null;
    this.length--;
    if (this.length === 0) {
      this.head = null;
      this.tail = null;
    }
    return currentNode;
  }

  public shift() {
    if (!this.head) return undefined;
    const currentHead = this.head;
    this.head = currentHead.next;
    this.length--;
    if (this.length === 0) {
      // no need to reset head because currentHead.next should be null to be the only node.
      this.tail = null;
    }
    return currentHead;
  }

  public unshift(val: T) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }

    this.length++;
    return this;
  }

  public get(index: number) {
    if (!this.head) return null;
    if (index < 0 || index >= this.length) throw Error('index out of range.');
    let node = this.head;
    let currentIndex = 0;

    while (node.next && currentIndex < index) {
      node = node.next;
      currentIndex++;
    }

    return node;
  }

  public set(val: T, index: number) {
    const node = this.get(index);
    if (node) {
      node.val = val;
    } else {
      throw Error('could not find the node to set');
    }
    return this;
  }
}

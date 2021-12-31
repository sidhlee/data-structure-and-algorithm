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
    return currentNode.val;
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
    return currentHead.val;
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
    if (!this.head) return undefined;
    if (this._isIndexInvalid(index)) return undefined;

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

  public insert(val: T, index: number) {
    if (index === 0) {
      this.unshift(val);
    } else if (index === this.length) {
      this.push(val);
    } else {
      const prevNode = this.get(index - 1);
      if (!prevNode) throw Error('could not find the previous node');
      const newNode = new Node(val);
      newNode.next = prevNode.next;
      prevNode.next = newNode;
      this.length++;
    }

    return this;
  }

  public remove(index: number) {
    if (this._isIndexInvalid(index)) return undefined;
    if (index === 0) return this.shift();
    if (index === this.length - 1) return this.pop();

    const prevNode = this.get(index - 1)!;
    if (prevNode.next) {
      // there are at least two nodes
      const nodeValue = prevNode.next.val;
      if (prevNode.next.next) {
        // there are at least three nodes
        prevNode.next = prevNode.next.next;
      }
      this.length--;
      return nodeValue;
    }
  }

  public reverse() {
    // list with one or no nodes are already reversed.
    if (this.head && this.head.next && this.tail) {
      // iterate from the second node
      let prevNode = this.head;
      let currentNode = this.head.next as Node<T> | null;
      let nextNode;

      while (currentNode) {
        nextNode = currentNode.next; // store next temporarily to iterate
        currentNode.next = prevNode; // update currentNode to point to prevNode

        prevNode = currentNode; // advance prevNode using current node
        currentNode = nextNode; // advance currentNode using stored next node
      }
      // swap head with tail
      const temp = this.head;
      this.head = this.tail;
      this.tail = temp;
      this.tail.next = null;
    }
    return this;
  }

  private _isIndexInvalid(index: number) {
    return index < 0 || index >= this.length;
  }
}

// h         t
// 1 -> 2 -> 3
// p    c    n
//   <-
//      p

import Node from './node';

export default class DoublyLinkedList<T> {
  length: number;
  head: Node<T> | null;
  tail: Node<T> | null;
  constructor() {
    this.length = 0;
    this.head = null;
    this.tail = null;
  }

  public push(val: T) {
    const newNode = new Node(val);
    if (!this.tail) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }

  public pop() {
    if (!this.tail) return undefined;
    const tailValue = this.tail.val; // store tail value
    this.tail = this.tail.prev; // update tail with prev value
    if (this.tail) {
      this.tail.next = null; // if prev node exist, update its next
    }
    this.length--;
    if (this.length === 0) {
      this.head = null;
    }
    return tailValue;
  }

  public shift() {
    if (!this.head) return undefined;
    const oldHead = this.head;
    this.head = oldHead.next;
    if (this.head) {
      this.head.prev = null;
    }
    this.length--;
    if (this.length === 0) {
      // no need to reset head because currentHead.next should be null to be the only node.
      this.tail = null;
    }
    return oldHead.val;
  }

  public unshift(val: T) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head.prev = newNode;
      this.head = newNode;
    }

    this.length++;
    return this;
  }

  public get(index: number) {
    if (!this.head || !this.tail) return undefined;
    if (this._isIndexInvalid(index)) return undefined;

    if (index < this.length / 2) {
      let node = this.head;
      let currentIndex = 0;
      while (node.next && currentIndex < index) {
        node = node.next;
        currentIndex++;
      }
      return node;
    } else {
      let node = this.tail;
      let currentIndex = this.length - 1;
      while (node.prev && currentIndex > index) {
        node = node.prev;
        currentIndex--;
      }
      return node;
    }
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
      newNode.prev = prevNode;
      if (prevNode.next) {
        prevNode.next.prev = newNode;
      }
      prevNode.next = newNode;

      this.length++;
    }

    return this;
  }

  public remove(index: number) {
    if (this._isIndexInvalid(index) || this.length === 0) return undefined;
    if (index === 0) return this.shift();
    if (index === this.length - 1) return this.pop();

    const removedNode = this.get(index)!;
    if (removedNode.prev) {
      removedNode.prev.next = removedNode.next;
    }
    if (removedNode.next) {
      removedNode.next.prev = removedNode.prev;
    }
    this.length--;
    return removedNode.val;
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

type Comparable = string | number;

export class Node {
  left: Node | null;
  right: Node | null;
  constructor(public value: Comparable) {
    this.left = null;
    this.right = null;
  }
}

export class BinarySearchTree {
  root: Node | null;
  constructor() {
    this.root = null;
  }

  insert(value: Comparable) {
    const newNode = new Node(value);
    if (!this.root) {
      this.root = newNode;
    } else {
      let currentNode: Node | null = this.root;
      while (currentNode) {
        if (value < currentNode.value) {
          if (currentNode.left) {
            currentNode = currentNode.left;
          } else {
            currentNode.left = newNode;
            currentNode = null;
          }
        } else if (value > currentNode.value) {
          if (currentNode.right) {
            currentNode = currentNode.right;
          } else {
            currentNode.right = newNode;
            currentNode = null;
          }
        }
      }
    }
    return this;
  }

  find(value: Comparable) {
    if (!this.root) return undefined;
    let currentNode = this.root;
    while (currentNode) {
      if (currentNode.value === value) {
        return currentNode;
      } else if (value < currentNode.value && currentNode.left) {
        currentNode = currentNode.left;
      } else if (value > currentNode.value && currentNode.right) {
        currentNode = currentNode.right;
      } else {
        return undefined;
      }
    }
  }
}

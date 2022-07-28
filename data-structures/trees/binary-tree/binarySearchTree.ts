import { Queue } from '../../queues/queue';

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

    if (this.root === null) {
      this.root = newNode;
      return this;
    }

    let currentNode = this.root;

    while (currentNode) {
      if (newNode.value < currentNode.value) {
        if (currentNode.left === null) {
          currentNode.left = newNode;
          break;
        } else {
          currentNode = currentNode.left;
        }
      } else if (newNode.value > currentNode.value) {
        if (currentNode.right === null) {
          currentNode.right = newNode;
          break;
        } else {
          currentNode = currentNode.right;
        }
      } else {
        throw new Error('Duplicated key is invalid in BST');
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

  /** returns an array of all nodes traversed with BFS */
  breadthFirstSearch() {
    if (!this.root) return [];
    const visitedNodeValues: Comparable[] = [];
    const queue = new Queue<Node>();
    queue.enqueue(this.root);
    while (queue.size > 0) {
      const currentNode = queue.dequeue();
      if (currentNode) {
        visitedNodeValues.push(currentNode.value);
        if (currentNode.left) {
          queue.enqueue(currentNode.left);
        }
        if (currentNode.right) {
          queue.enqueue(currentNode.right);
        }
      }
    }

    return visitedNodeValues;
  }

  depthFirstPreOrder() {
    if (!this.root) return [];
    const visitedNodeValues: Comparable[] = [];

    function traverse(node: Node) {
      if (!node) return;
      visitedNodeValues.push(node.value);
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
    }
    traverse(this.root);

    return visitedNodeValues;
  }

  depthFirstPostOrder() {
    if (!this.root) return [];
    const visitedNodeValues: Comparable[] = [];

    function traverse(node: Node) {
      if (!node) return;
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
      visitedNodeValues.push(node.value);
    }
    traverse(this.root);

    return visitedNodeValues;
  }

  depthFirstInOrder() {
    if (!this.root) return [];
    const visitedNodeValues: Comparable[] = [];

    function traverse(node: Node) {
      if (!node) return;
      if (node.left) traverse(node.left);
      visitedNodeValues.push(node.value);
      if (node.right) traverse(node.right);
    }
    traverse(this.root);

    return visitedNodeValues;
  }
}

import { Node, BinarySearchTree } from './binarySearchTree';

describe('Node', () => {
  it('has left, right and value', () => {
    const node = new Node('item');
    expect(node.left).not.toBeUndefined();
    expect(node.right).not.toBeUndefined();
    expect(node.value).not.toBeUndefined();
  });
});

describe('BinarySearchTree', () => {
  it('has root', () => {
    const bst = new BinarySearchTree();
    expect(bst.root).not.toBeUndefined();
  });

  describe('insert', () => {
    let bst: BinarySearchTree;
    beforeEach(() => {
      bst = new BinarySearchTree();
    });
    it('creates a new root node when ', () => {
      bst.insert(0);
      expect(bst.root?.left).not.toBeUndefined();
      expect(bst.root?.right).not.toBeUndefined();
    });

    it('inserts to the correct location', () => {
      bst
        .insert(10)
        .insert(5)
        .insert(7)
        .insert(3)
        .insert(6)
        .insert(15)
        .insert(13);
      expect(bst.root?.left?.value).toBe(5);
      expect(bst.root?.left?.left?.value).toBe(3);
      expect(bst.root?.left?.left?.left).toBe(null);
      expect(bst.root?.left?.left?.right).toBe(null);
      expect(bst.root?.left?.right?.value).toBe(7);
      expect(bst.root?.left?.right?.left?.value).toBe(6);
      expect(bst.root?.left?.right?.right).toBe(null);
      expect(bst.root?.right?.value).toBe(15);
      expect(bst.root?.right?.left?.value).toBe(13);
      expect(bst.root?.right?.left?.left).toBe(null);
      expect(bst.root?.right?.left?.right).toBe(null);
      expect(bst.root?.right?.right).toBe(null);
    });

    it('returns the instance', () => {
      expect(bst.insert(0)).toBe(bst);
    });
  });

  describe('find', () => {
    let bst: BinarySearchTree;
    beforeEach(() => {
      bst = new BinarySearchTree();
    });
    it('returns undefined if tree is empty', () => {
      expect(bst.find('')).toBe(undefined);
    });
    it('returns undefined if the value cannot be found', () => {
      bst.insert(0);
      expect(bst.find(100)).toBe(undefined);
    });

    it('return the found node', () => {
      bst
        .insert(10)
        .insert(5)
        .insert(7)
        .insert(3)
        .insert(6)
        .insert(15)
        .insert(13);
      const node = bst.find(6);
      expect(node?.value).toBe(6);
      expect(node?.left).toBeNull();
      expect(node?.right).toBeNull();
    });
  });

  describe('breadthFirstSearch', () => {
    let bst: BinarySearchTree;
    beforeEach(() => {
      bst = new BinarySearchTree();
    });
    it('returns an empty array when the tree is empty', () => {
      expect(bst.depthFirstPreOrder()).toEqual([]);
    });

    it('returns an array of all nodes traversed with BFS', () => {
      bst
        .insert(10)
        .insert(5)
        .insert(7)
        .insert(3)
        .insert(6)
        .insert(15)
        .insert(13);
      expect(bst.breadthFirstSearch()).toEqual([10, 5, 15, 3, 7, 13, 6]);
    });
  });

  describe('depthFirstPreOrder', () => {
    let bst: BinarySearchTree;
    beforeEach(() => {
      bst = new BinarySearchTree();
    });
    it('returns an empty array when the tree is empty', () => {
      expect(bst.depthFirstPreOrder()).toEqual([]);
    });

    it('returns the array of traversed node values', () => {
      bst
        .insert(10)
        .insert(5)
        .insert(7)
        .insert(3)
        .insert(6)
        .insert(15)
        .insert(13);
      expect(bst.depthFirstPreOrder()).toEqual([10, 5, 3, 7, 6, 15, 13]);
    });
  });

  describe('depthFirstPostOrder', () => {
    let bst: BinarySearchTree;
    beforeEach(() => {
      bst = new BinarySearchTree();
    });
    it('returns an empty array when the tree is empty', () => {
      expect(bst.depthFirstPostOrder()).toEqual([]);
    });

    it('returns the array of traversed node values', () => {
      bst
        .insert(10)
        .insert(5)
        .insert(7)
        .insert(3)
        .insert(6)
        .insert(15)
        .insert(13);
      expect(bst.depthFirstPostOrder()).toEqual([3, 6, 7, 5, 13, 15, 10]);
    });
  });

  describe('depthFirstInOrder', () => {
    let bst: BinarySearchTree;
    beforeEach(() => {
      bst = new BinarySearchTree();
    });
    it('returns an empty array when the tree is empty', () => {
      expect(bst.depthFirstInOrder()).toEqual([]);
    });

    it('returns the array of traversed node values', () => {
      bst
        .insert(10)
        .insert(5)
        .insert(7)
        .insert(3)
        .insert(6)
        .insert(15)
        .insert(13);
      expect(bst.depthFirstInOrder()).toEqual([3, 5, 6, 7, 10, 13, 15]);
    });
  });
});

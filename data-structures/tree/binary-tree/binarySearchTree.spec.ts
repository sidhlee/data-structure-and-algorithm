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
});

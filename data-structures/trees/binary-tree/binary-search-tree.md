# Binary Search Tree

A Binary Search Tree is a Binary Tree with sorted data where the left child always has smaller value than the parent and the right child always has a value greater than its parent.

- Right node's left child is always less than the node's value and greater than the node's parent.
- When traversing in straight line, left child is always smaller than its parent, and right child is always greater than its parent.
- When changing the direction of the traversal, the first child that with the changed direction always has the value between its parent and the grandparent.

## Binary Tree

In Binary trees, each node can have have maximum two nodes.

### Full Binary Tree

A Full Binary Tree is a tree where every node other than leaves have two children, left and right.

```text
       Root
    L        R
 L    R    L    R
L R  L R  L R  L R
```

### Complete Binary Tree

A Complete Binary Tree is a tree where every level except possibly the last is completely filled from left to right.

```text
       Root
    L        R
 L    R    L    R
L R  L
```

### Balanced Binary Tree

A Balanced Binary Tree is a tree where every node has left and right subtree whose heights do not differ greater than one.
In the following chart, the number indicates the difference between the height of the left and right subtrees.

```text
       0
   1       1
 1   1   0   1
0     0     0
```

## BST methods

### BST Insert

Insert with Binary Search Tree can be implemented either recursively or iteratively.

### BST Find

Finds and returns the node that matches the given value.

## BST Complexities

Binary Search Trees offer O(log(n)) time for average search, insert and delete operation where the tree is balanced.
The worst case is when the tree only has either left or right node and it's O(n) because you need to go through the entire tree to reach the leaf.

## DFS for BST

Unlike Breadth First Search whose implementation can be applied to any tree structure regardless of the number of children, there are three different types of DFS that can be applied to the Binary Search Tree more easily.

- [Animated pseudocode](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/BinaryTreeTraversal.html)

### Pre-Order Traversal

Pre-order traversal processes data before visiting children.
Nodes are processed from top to bottom, left to right.
Pre-order traversal is good when you need to process the nodes outward from the root.

- Processes data before visiting children
- The Left-most leaf is visited first
- Backtracks to find node with right child repeat the search
- After visiting the right-most leaf, it backtracks to the root node.

```js
function preorder(node) {
  if (!node) return;
  process(node);
  preorder(node.left);
  preorder(node.right);
}
```

Pre-order can be useful when you want to store and reconstruct a tree because we can identify the root at the beginning of the array.

### Post-Order Traversal

Post-order traversal processes data after visiting both children. This is useful when you need to remove all children before deleting the current node.
After traversing to the left-most leaf, it tries to process all direct sibling before moving up to processing the parent.
Post-order traversal is useful when you need to traverse from the leaf toward the root.

- Processes data after visiting both left and right children including the empty nodes on the leaf.
- The Left-most leaf is visited & processed first.
- Then traverse to the right sibling via parent and process it before the parent.
- The right-most branch is process at the end from the leaf node to the root.

```js
function preorder(node) {
  if (!node) return;
  preorder(node.left);
  preorder(node.right);
  process(node);
}
```

### In-Order Traversal

In-order traversal travels down to the left until it visits the node without the left child and processes it. Then it backtrack to its parent to process and finally to that parent's right child. With Binary Search Tree, in-order traversal allows you to process the nodes from the smallest value in ascending order.

1. Keep going down to the left until there is no left and process it.
2. If the processed node has the right child go back to 1.
3. Else, backtrack to parent and process.
4. Go back to 2.

```js
function preorder(node) {
  if (!node) return;
  preorder(node.left);
  process(node);
  preorder(node.right);
}
```

## DFS for Non-Binary Trees

For non-binary trees, you can do post-order/in-order traversal like so:

```ts
function traverse(node: Node) {
  if (!node) return;
  // printData(node.value) // pre-order
  node.getChildren().forEach((childNode) => {
    traverse(childNode);
  });
  printData(node.value); // post-order
}
```

In-order traversal for non-binary tree seems to have different implementations based on how it's defined.

- [Inorder traversal for an N-ary tree](https://www.geeksforgeeks.org/inorder-traversal-of-an-n-ary-tree/)
- [Inorder traversal for non binary trees](https://stackoverflow.com/questions/23778489/in-order-tree-traversal-for-non-binary-trees)

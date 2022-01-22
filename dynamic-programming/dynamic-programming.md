# Dynamic Programming

With dynamic programming, you can solve a complex problem by breaking it down to smaller, overlapping sub-problems and storing their solutions to avoid duplicating calculations.

## When can we use dynamic programming

There are two conditions that call for dynamic programming:

- optimal sub-structure - an optimal solution can be constructed from optimal solutions of its sub-problems
  - Fibonacci Sequence
  - Dijkstra's shortest path algorithm - the shortest path from A to D is also the shortest path from A to C.
- overlapping sub-problems

## Example of no-optimal sub-structure

- Finding the longest simple (non-repeating) path - we can't re-use the solutions to the sub-problems

  - A -> C : A > B > C
  - C -> D : C > B > D
  - A -> D is NOT A > B > C > B > D, but A > B > D

- Finding the cheapest route from two cities - tickets might not be available for stop-overs, might introduce long wait time, etc...
  - Airlines are trying their best to block the loophole.

## Example of non-overlapping sub-problems

- Merge Sort - overlap only happens when there are repeated values evenly spaced. (eg. mergeSort([10, 24, 10, 24]))

## Fibonacci Sequence

In Fibonacci sequence, every number after the first two are the sum of the two preceding ones.

### Fibonacci Sequence - Recursive solution

The base case is when n <=2, in which case we return 1.
The recursive solution involves a lot of overlapping calculations, and the number of sub-problems grows at O(2^n). (or O(1.6^n) with some math). This exponential complexity is due to the fact that the function calls itself twice in one stack frame, and the number passed approaches to the base case linearly.

- To get fib(5), we add the results of fib(4) and fib(3)
- To get fib(4), we add the results of fib(3) and fib(2)
- To get fib(3), we add the results of fib(2) and fib(1)
- and so on...

There is a lot of repeated calculations for the same input. The call stack can be represented with a binary tree where every right child and its subtree is the exact duplication of left child's subtree.

### Fibonacci Sequence - With Memoization

By memoizing the return value of the function, we can effectively eliminate all the right children of the binary tree. This leave only the left-most branch, which gives us O(n) complexity.

### Fibonacci Sequence - With Tabulation

In contrast to the top-down approach of memoization, we can use a technique called **Tabulation**, which is a bottom-up approach.

- Usually implemented with iteration
- Store the previous result to a "table" (usually an array)
- Better space complexity (doesn't rely on a call stack)

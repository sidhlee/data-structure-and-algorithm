# Multiple Pointers Pattern

In multiple pointers pattern, we create pointers to hold the position of items inside arrays and move them to the beginning, end, or middle based on a certain condition.
Patterns with pointers usually work **in place**, so very efficient with space complexity.

## sumZero

Write a function called `sumZero` which accepts a sorted array of integers. The function should find the first pair where the sum is 0. Return an array that includes both values that sum to zero or undefined if the pair does not exist.

```js
sumZero([-3, -2, -1, 0, 1, 2, 3]); // [-3, 3]
sumZero([-2, 0, 1, 3]); // undefined
sumZero([1, 2, 3]); // undefined
```

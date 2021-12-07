# Sliding Window Pattern

Sliding Window pattern is useful when we try to find a continuous subset of an iterable (eg. array, string, etc...).
We can slide The "window" or the subset while we're keeping track of it and the size of the window can grow and shrink based on certain conditions.

## maxSubarraySum

Write a function called maxSubarraySum which accepts an array of integers and a number n. The function should calculate the maximum sum of n consecutive numbers in the array.

```js
maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 2); // 10
maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 4); // 17
maxSubarraySum([4, 2, 1, 6], 1); // 6
maxSubarraySum([4, 2, 1, 6, 2], 4); // 13
maxSubarraySum([], 4); // null
```

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

## minSubarrayLen

Write a function called `minSubarrayLen` which accepts an array of integers and a positive integer.
This function should return the minimal length of a continuous subarray of which the sum is greater than or equal to the integer passed to the function. If there isn't one, return 0 instead.

### Constraints

- Time: O(n)
- Space: O(1)

```js
minSubarrayLen([2, 3, 1, 2, 4, 3], 7); // 2 -> [4, 3] is the smallest subarray
minSubarrayLen([2, 1, 6, 5, 4], 9); // 2 -> [5, 4] is the smallest subarray
minSubarrayLen([3, 1, 7, 11, 2, 9, 8, 21, 62, 33, 19], 52); // 1 -> [62] is greater than 52
minSubarrayLen([4, 3, 3, 8, 1, 2, 3], 11); // 2
minSubarrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 39); // 3
minSubarrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 55); // 5
minSubarrayLen([1, 4, 16, 22, 5, 7, 8, 9, 10], 95); // 0
```

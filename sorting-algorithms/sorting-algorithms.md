# Sorting Algorithm

## Bubble Sort

Bubble Sort swaps adjacent elements to bubble up the largest values to the top (or end of the list). After bubbling up the largest value to the top, it goes through the list again to bubble up the second largest value up to the second last place, just before the previously bubbled up value. The list to loop through gets reduced after each iteration until only the smallest value remain at the beginning.

### Bubble Sort Pseudocode

- Start looping from the end of the array towards the beginning.
- Start inner loop from the beginning up to the outer cursor, swapping the adjacent items if the item has greater value than the next item. This will place the largest value within the inner loop to the end of the range, and eliminate that value from the next run through the inner loop.kli,m.
- Return the sorted array
- You can further optimize by returning early if there was no swaps in previous iteration meaning the array is already sorted.

### Bubble Sort Complexity

- Worst case: O(n^2) - start with reverse sorted array
- Best case: O(n) - start with already sorted array
- Space: O(1)

## Selection Sort

Selection sort finds the minimum value while looping through an array and selectively swap it with the starting value of the subarray. The inner loop or the subarray becomes smaller by excluding the swapped smallest value from the previous iteration.

### Selection Sort Pseudocode

- Store the first element as the min value
- Compare this item to the next item until you find the smallest value
- If new min value is found, swap it with the old min value at the beginning of the loop.
- Repeat from the second item in teh array.

### Selection Sort Complexity

- O(n^2) - always need to check "the next smallest number" from each iteration through the outer loop.
- Space: O(1)

### Selection Sort vs Bubble Sort

- Selection sort swaps maximum once per iteration through the inner loop.
  - This might be desirable in a situation where swapping is expensive (eg. taking too much memory)
- Bubble sort swaps maximum n - 1 times where n is the size of the inner loop.
- You can optimize bubble sort by breaking out of the outer loop when there's no swapping in the inner loop.
- You need to complete the outer loop with the selection sort to find the minimum value.

## Insertion Sort

Insertion sort iterates through the array and inserts each item into the sorted subarray to its left. This works great when new item is continuously being added to the already sorted array.

### Insertion Sort Pseudocode

- Start from the second item in the array.
- Insert the item to the right place in the subarray to the left where the first item in the array is already included.
- No need to swap if the last item in the subarray is smaller than the one being inserted because the subarray is always sorted.
- Repeat until the end of the array is reached.

### Insertion Sort Complexity

- Worst case: O(n^2) - sorting reverse sorted array
- Best case: O(n) - when adding an item to be already sorted array

## Merge Sort

Merge sort recursively splits an array into two until the subarray becomes empty or only has one item. Once it reaches the base case, it starts backtracking while merging two sorted subarrays into one sorted array. This process takes advantage of the fact that the array of one or zero item is always sorted.

### Merging arrays Pseudocode

These are the steps to implement merging function that takes two sorted arrays and merge them into one sorted array.

- Create an empty result array and two pointers for the arrays to merge.
- While both pointers are within the range:
  - compare values at the pointers and push smaller value to the result array. Advance the pointer for the array that had the smaller value.
- When one of the pointers reach the end of the array, we break out of the loop and push all remaining elements into the results because they are already sorted AND greater than the values already in the results.

### Merge Sort Complexity

- Time: O(n log(n)) - log(n) for splitting in half \* n for sorting and merging
- Space: O(n) - n + (n/2 + n/2) + (n/4 + n/4) ... = C \* n = n

## Quick Sort

Quick Sort picks a pivot, in our case the first item in the array, and finds the index it needs to go after sending all items smaller than the pivot to the left of it and all items greater to the right. Then, it identifies two subarrays, the one before the pivot and the other after, and applies the same process for the subarrays until the subarray's length becomes less than one. Quick Sort always mutates the original array _in place_, so it needs two more arguments other than the array being sorted to indicate the beginning of the subarray and the end. Because it calls itself sequentially for the left subarray and the right, the original array gets sorted in depth-first order while traversing a binary tree branching down into left and right.

### Pivot Pseudocode

We need a helper function named `pivot` to call inside the `quickSort` function with the left and the right subarray. `pivot` takes an array, a start index and an end index to indicate the range of items being sorted. After rearranging the items around the pivot, it returns the index of the pivot where the items smaller than the pivot are placed to the left and the items greater than the pivot to the right.

- Pick the first item of the range to be the pivot ie. the item at the `startIndex`
- Create the `pivotIndex` and initialize it with the value of the `startIndex`.
  - `pivotIndex` does not care about the value happens to be at the index while looping. It is just to keep track of the number of items smaller than the pivot.
- Loop through the array from the start until the end index
  - If the current item is smaller than the pivot, increment the `pivotIndex` and swap the current item with the item at the `pivotIndex`.
  - The current item will end up in the same position if there is no item whose value is greater than the pivot value.
  - For example, `pivotIndex` of 4 means that after sorting the given range of the array, there will be 4 items (at index 0, 1, 2, and 3) smaller than the pivot regardless of their order.
- After we reach the end of the loop, swap the pivot with the item at the pivot index.
- `pivot` function does not care about the order of items in either side of the pivot. Its return value only indicates the position of the pivot within the given range and we know that any value smaller than the pivot is placed to the left and any item greater to the right.

### Quick Sort Implementation

- Call `pivot` to rearrange the array and get the `pivotIndex`.
  - You can set the default value for start and end index for the `quickSort` so that you don't need to pass in `0` and `array.length - 1` as you call it.
- Call `pivot` with the end index being the `pivotIndex` - 1.
  - This path will repeat until the left most path reaches the end of the tree where start index is equal to the end index.
  - Then it will backtrack to traverse to the "right" side of the tree.
- Call `pivot` with the start index being the `pivotIndex` + 1.
- After finishing backtracking, it will return the sorted array.
- Need the base case of start index greater than or equal to the end index. It will return the input array as is when that happens.

### Quick Sort Complexity

Quick Sort performs best when the pivot is chosen to be the median value of the given range. It performs worst at O(n^2) when the pivot is chosen to be min or max value so that there is only one partition available recursively. You can randomize where to pick the pivot to avoid the worst case.

- Time(best & average): O(n log(n)) - n for looping from start to end index, log(n) for calling itself with left and right range.
- Time(worst): O(n^2) - pivot is chosen to be first or last item, so we only have either left or right side. The deepest path in tree becomes as long as n

## Radix Sort

While the comparison sort algorithm has the lower bound of n log(n) time complexity, Radix sort is a non-comparison sort that utilizes a special property of integers where numbers with more digits are always greater than numbers with less digits.
Radix sort distributes numbers in the list to the buckets 0 to 9 based on the the number's least significant digit and push them back to the array in the order they are stored in the buckets. As we repeat the same steps with n-th digit from the right, the numbers with n number of digits becomes sorted among themselves, and the numbers whose number of digits are less than n get stored in the bucket 0, already sorted in the previous iterations.
It takes only as many iterations as the maximum number of digits found in the list to complete the sorting.

### Radix Sort Helpers

- `getDigit(num, place)` - returns the digit in `num` at the given `place` value.
- `countDigits(num)` - returns the number of digits in `num`.
- `getMaxDigit(nums)` - returns the maximum number of digits that can be found in the given array of numbers.

### Radix Sort Implementation

- Loop from i=0 while i <= k where k is the maximum number of digits found in the input array. In each iteration:
  - create the buckets from 0 to 9
  - place numbers in the bucket based on its i-th digit
  - Replace the input array with the values from the buckets going from 0 to 9
- Return the array

### Radix Sort Complexity

- Time (best, average, worst) - O(nk) where k is max number of digits
- Space - O(n + k) where k is the number of unique numbers(eg. k = 10 for base 10)

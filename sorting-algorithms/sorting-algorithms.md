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

## Selection Sort

Selection sort finds the minimum value while looping through an array and selectively swap it with the starting value of the subarray. The inner loop or the subarray becomes smaller by excluding the swapped smallest value from the previous iteration.

### Selection Sort Pseudocode

- Store the first element as the min value
- Compare this item to the next item until you find the smallest value
- If new min value is found, swap it with the old min value at the beginning of the loop.
- Repeat from the second item in teh array.

### Selection Sort vs Bubble Sort

- Selection sort swaps maximum once per iteration through the inner loop.
  - This might be desirable in a situation where swapping is expensive (eg. taking too much memory)
- Bubble sort swaps maximum n - 1 times where n is the size of the inner loop.
- You can optimize bubble sort by breaking out of the outer loop when there's no swapping in the inner loop.
- You need to complete the outer loop with the selection sort to find the minimum value.

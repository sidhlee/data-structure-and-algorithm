# Sorting Algorithm

## Bubble Sort

Bubble Sort swaps adjacent elements to bubble up the largest values to the top (or end of the list). After bubbling up the largest value to the top, it goes through the list again to bubble up the second largest value up to the second last place, just before the previously bubbled up value. The list to loop through gets reduced after each iteration until only the smallest value remain at the beginning.

- Start looping from the end of the array towards the beginning.
- Start inner loop from the beginning up to the outer cursor, swapping the adjacent items if the item has greater value than the next item. This will place the largest value within the inner loop to the end of the range, and eliminate that value from the next run through the inner loop.kli,m.
- Return the sorted array
- You can further optimize by returning early if there was no swaps in previous iteration meaning the array is already sorted.

### Complexity

- Worst case: O(n^2) - start with reverse sorted array
- Best case: O(n) - start with already sorted array

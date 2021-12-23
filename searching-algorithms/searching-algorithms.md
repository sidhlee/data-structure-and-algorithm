# Searching Algorithms

## Linear Search

Linear search has the time complexity of O(n).

## Binary Search

- Only works on SORTED arrays.
- Has O(log(n)) time.
- Eliminates the half of the array with each iteration.

## Naive String Search

Returns the number of times shorter string is found in the longer string using the following strategy:

- Loop over the longer string until it matches the first character in the shorter string
- Loop over the shorter string to see the characters coming after matches the entire string.
- If not, break out of the inner loop.
- If matches, continue
- When the inner loop is completed, you found a match. increment counter.

## KMP

def minimumSwaps_send_to_correct_position(arr):
    """
    2023-02-04 11:57:53
    Uses the assumption that the given array contains sequential integers starting at 1.
    Final sorted array should be [1, 2, 3, ..., n]
    We can infer the correct position of the item by its value.
    - if 3 is at index 0, it should eventually go to index position 2
    - repeat sending the value at the correct position until the current value
      matches the current index + 1.

    Using selection sort is the wrong approach and takes quadratic time
    - while iterating through the array
    - searching minimum value from the array starting from i and swap
    This is unnecessary because we already know that the minimum value will always be 1.
    Also we know that next min value is going to be sequential.
    """
    swaps = 0
    curr_idx = 0
    while curr_idx < len(arr):
        if arr[curr_idx] == curr_idx + 1:
            curr_idx += 1
        else:
            sorted_idx = arr[curr_idx] - 1
            arr[curr_idx], arr[sorted_idx] = arr[sorted_idx], arr[curr_idx]
            swaps += 1
    return swaps


minimum_swaps = minimumSwaps_send_to_correct_position

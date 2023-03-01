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


def minimumSwaps(arr):
    count = 0
    i = 0
    while i < len(arr) - 1:
        o_idx = arr[i] - 1
        if o_idx == i:
            i += 1
        else:
            arr[i], arr[o_idx] = arr[o_idx], arr[i]
            count += 1
    return count


def minimumSwaps_fails_using_dynamic_indexing(arr):
    """
    2023-03-01 08:01:58
    This one results in a infinite loop because it's getting index position from the newly swapped value.
    Pythonic swap with tuple only works if you save the swapping index into a variable.

    [output]
    # starting values
    i: 0, arr: [4, 3, 1, 2], count: 0
    # arr[arr[i] - 1 -> 3](2) is copied to index 0, but arr[i](4) is copied to the new arr[i] - 1(1).
    i: 0, arr: [2, 4, 1, 2], count: 0
    # arr[arr[i] - 1 -> 1](4) is copied to index 0, and arr[i](2) is copied to the new arr[i] - 1(3).
    i: 0, arr: [4, 4, 1, 2], count: 1
    # arr[arr[i] - 1 -> 3](2) is copied to index 0, and arr[i](4) is copied to the new arr[i] - 1(1).
    i: 0, arr: [2, 4, 1, 2], count: 2
    i: 0, arr: [4, 4, 1, 2], count: 3
    ...


    """
    count = 0
    i = 0
    print(f"i: {i}, arr: {arr}, count: {count}")
    while i < len(arr) - 1:
        if arr[i] - 1 == i:
            i += 1
        else:
            arr[i], arr[arr[i] - 1] = arr[arr[i] - 1], arr[i]
            print(f"i: {i}, arr: {arr}, count: {count}")
            count += 1

    return count


minimum_swaps = minimumSwaps_send_to_correct_position

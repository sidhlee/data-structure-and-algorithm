from typing import List, Union


def max_subarray_sum(numbers: List[int], size: int) -> Union[int, None]:
    """Calculates the maximum sum of the subarray of the given size

    Args:
        numbers: a list of integers
        size: the size fo subarray

    Returns:
        int: the sum of the subarray. None if the array is empty
    """
    if size > len(numbers):
        return None
    current_sum = sum(numbers[0:size])
    max_sum = current_sum
    for i in range(1, len(numbers) - size):
        removing_number = numbers[i - 1]
        adding_number = numbers[i + size - 1]
        current_sum = current_sum - removing_number + adding_number
        max_sum = max(max_sum, current_sum)

    return max_sum


def where_to_grow(numbers: List[int], head_index: int, tail_index: int) -> int:
    try:
        left = numbers[head_index - 1]
    except IndexError:
        left = -1
    try:
        right = numbers[tail_index + 1]
    except IndexError:
        right = -1
    if left < 0 and right < 0:
        return 0
    elif left < 0 or left < right:
        return 1
    else:
        return -1


def min_subarray_len(numbers: List[int], min: int) -> int:
    # Invalidate and return early!
    if sum(numbers) < min:
        return 0
    subarray_len = 0
    subarray_sum = 0
    try:
        max_number = max(numbers)
    except ValueError:  # given an empty list
        return 0
    max_index = numbers.index(max_number)
    subarray_sum += max_number
    subarray_len += 1
    subarray_head_index = max_index
    subarray_tail_index = max_index
    while subarray_head_index >= 0 and subarray_tail_index < len(numbers):
        if subarray_sum >= min:
            return subarray_len
        direction = where_to_grow(numbers, subarray_head_index, subarray_tail_index)
        if direction == -1:
            subarray_head_index -= 1
            subarray_sum += numbers[subarray_head_index]
            subarray_len += 1
        elif direction == 1:
            subarray_tail_index += 1
            subarray_sum += numbers[subarray_tail_index]
            subarray_len += 1
        else:
            return 0

    return subarray_len

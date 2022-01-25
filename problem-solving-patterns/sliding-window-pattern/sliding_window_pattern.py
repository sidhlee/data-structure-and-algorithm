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

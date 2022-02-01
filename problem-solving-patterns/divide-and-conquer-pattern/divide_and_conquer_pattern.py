from math import floor
from typing import List


def binary_search_recursive(items: List[int], value: int) -> int:
    def inner(head_index: int, tail_index: int) -> int:
        if head_index > tail_index:
            return -1
        mid_index = floor((tail_index + head_index) / 2)
        mid_value = items[mid_index]
        if value == mid_value:
            return mid_index
        elif mid_value < value:
            return inner(mid_index + 1, tail_index)
        else:
            return inner(head_index, mid_index)

    return inner(0, len(items) - 1)


def binary_search_iterative(items: List[int], value: int) -> int:

    head_index = 0
    tail_index = len(items) - 1

    while head_index <= tail_index:
        mid_index = floor((head_index + tail_index) / 2)
        mid_value = items[mid_index]
        if mid_value == value:
            return mid_index
        elif mid_value < value:
            head_index = mid_index + 1
        else:
            tail_index = mid_index
    return -1

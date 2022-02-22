from abc import ABCMeta, abstractmethod
from typing import Any, List, TypeVar


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)


def swap(arr: List[Any], index1: int, index2: int):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def get_max_entry(arr: List[CT]):
    current_max_index = 0
    current_max = arr[current_max_index]
    for index, value in enumerate(arr):
        if value > current_max:
            current_max_index = index
            current_max = arr[current_max_index]
    return (current_max_index, current_max)


def bubble_sort_while(arr: List[CT]) -> List[CT]:
    result = arr.copy()
    tail_index = len(arr) - 1
    while tail_index > 0:
        (max_index, _) = get_max_entry(result[0 : tail_index + 1])
        swap(result, max_index, tail_index)
        tail_index -= 1
    return result


def bubble_sort(arr: List[CT]) -> List[CT]:
    copied_arr = arr.copy()
    for i in range(len(copied_arr) - 1, 0, -1):
        has_been_swapped = False
        # i is the index of the last element in the subarray
        for j in range(i):
            if copied_arr[j] > copied_arr[j + 1]:
                swap(copied_arr, j, j + 1)
                has_been_swapped = True
        # optimization: it's been already sorted, so didn't have to swap while looping through the entire subarray
        if not has_been_swapped:
            break
    return copied_arr


def get_min_entry(arr: List[CT]) -> int:
    min = arr[0]
    min_index = 0
    for i, val in enumerate(arr):
        if val < min:
            min = val
            min_index = i
    return min_index, min


def selection_sort(arr: List[CT]) -> List[CT]:
    copied_arr = arr.copy()
    for i in range(len(arr)):
        min_index_of_subarray, _ = get_min_entry(copied_arr[i:])
        min_index = min_index_of_subarray + i
        swap(copied_arr, min_index, i)
    return copied_arr


def insertion_sort_swap(arr: List[CT]) -> List[CT]:
    # if there is less than two items, it's already sorted
    if len(arr) < 2:
        return arr
    arr_copy = arr.copy()
    # the subarray should start from the array of one item because
    # it might be greater than the second item (inserting item)
    subarr_tail = 0
    # grow subarr each time until it becomes n - 1
    # because we're going to insert the item at n
    while subarr_tail < len(arr) - 1:
        # reset pointer to the last subarr item
        inserting_item_index = subarr_tail + 1
        # loop from the last item in the subarray to the first item
        for i in range(subarr_tail, -1, -1):
            # keep swapping until the left value is leq to the inserting item
            if arr_copy[i] > arr_copy[inserting_item_index]:
                # swap and update the inserting item index
                swap(arr_copy, inserting_item_index, i)
                inserting_item_index = i
            # if the last item is leq to the inserting item, we don't get into the nested loop
            else:
                break
        subarr_tail += 1
    return arr_copy


def insertion_sort(arr: List[CT]) -> List[CT]:
    if len(arr) < 2:
        # already sorted. return.
        return arr
    arr_copy = arr.copy()
    for inserting_item_index in range(1, len(arr)):
        inserting_item = arr_copy[inserting_item_index]
        # loop from the last item in the subarray back to the first item
        for curr_subarr_item_index in range(inserting_item_index - 1, -1, -1):
            curr_subarr_item = arr_copy[curr_subarr_item_index]
            if curr_subarr_item <= inserting_item:
                # Before breaking out of the inner loop, we need to increment the index
                # because that's where we're going to copy the inserting item
                curr_subarr_item_index += 1
                break
            else:
                arr_copy[curr_subarr_item_index + 1] = curr_subarr_item
                # if we finish the inner loop after copying the first subarray item to the right,
                # we have the current index pointing at the index 0
        arr_copy[curr_subarr_item_index] = inserting_item

    return arr_copy


def sort_and_merge(arr1: List[CT], arr2: List[CT]) -> List[CT]:
    return []


def merge_sort(arr: List[CT]) -> List[CT]:
    return []


def pivot(arr: List[CT], head_index: int, tail_index: int) -> int:
    pass


def quick_sort(arr: List[CT]) -> List[CT]:
    return []


def radix_sort(arr: List[CT]) -> List[CT]:
    return []

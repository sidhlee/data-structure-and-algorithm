from abc import ABCMeta, abstractmethod
from math import ceil, floor
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


def compare_and_sort(sorted_arr1: List[CT], sorted_arr2: List[CT]) -> List[CT]:
    result = []
    i = 0
    j = 0
    while i < len(sorted_arr1) and j < len(sorted_arr2):
        if sorted_arr1[i] < sorted_arr2[j]:
            result.append(sorted_arr1[i])
            i += 1
        else:
            result.append(sorted_arr2[j])
            j += 1
    if i >= len(sorted_arr1) and j < len(sorted_arr2):
        result += sorted_arr2[j:]
    if i < len(sorted_arr1) and j >= len(sorted_arr2):
        result += sorted_arr1[i:]

    return result


def merge_sort(arr: List[CT]) -> List[CT]:
    if len(arr) < 2:
        return arr

    mid = floor(len(arr) / 2)
    left = arr[0:mid]
    right = arr[mid:]

    # keep breaking the arr in half until there is a single item
    # backtrack to merge them into a single array.
    return compare_and_sort(merge_sort(left), merge_sort(right))


"""
[1, 5, 2, 8, -3, 0, -65] -> [-65, -3, 0, 1, 2, 5, 8]
len: 7
mid: 3
left: arr[0:3] -> [1, 5, 2] -> [1, 2, 5]
    len: 3
    mid: 1
    left: [1]
    right: [5, 2] -> [2, 5]
        len: 2
        mid: 1
        left: [5]
        right: [2]
right: arr[3:] -> [8, -3, 0, -65] -> [-65, -3, 0, 8]
    len: 4
    mid: 2
    left: [8, -3] -> [-3, 8]
        left: [8]
        right: [-3]
    right: [0, -65] -> [-65, 0]
        left: [0]
        right: [-65]
"""


def pivot(arr: List[CT], head_index: int = 0, tail_index: int = None) -> int:
    if tail_index is None:
        tail_index = len(arr) - 1

    pivot_index = head_index
    curr_index = pivot_index + 1
    while curr_index <= tail_index:
        if arr[curr_index] < arr[head_index]:
            swap(arr, curr_index, pivot_index + 1)
            # found smaller value, move index that pivot needs to move to
            pivot_index += 1
        curr_index += 1

    swap(arr, pivot_index, head_index)
    return pivot_index


"""
pi=0, ci=1, [5, 2, 13, 1, 4, 8] move 2 to index 1
pi=1, ci=2, [5, 2, 13, 1, 4, 8] 
pi=1, ci=3, [5, 2, 1, 13, 4, 8] move 1 to index 2 
pi=2, ci=4, [5, 2, 1, 4, 13, 8] move 4 to index 3
pi=3, ci=5, [5, 2, 1, 4, 13, 8]
pi=3, ci=6, ci out of range, break out of loop
swap 4 with 5 [4, 2, 1, 5, 13, 8]
"""


def quick_sort(arr: List[CT], head_index: int = 0, tail_index: int = None) -> List[CT]:
    # set default tail_index
    if tail_index is None:
        tail_index = len(arr) - 1
    # base case - less than or equal to 1 array item (tail is the last item)
    if tail_index - head_index < 1:
        return arr

    pivot_index = pivot(arr, head_index, tail_index)
    quick_sort(arr, head_index, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, tail_index)

    return arr


def flatten(array):
    flattened = []
    for subarray in array:
        for item in subarray:
            flattened.append(item)
    return flattened


def get_num_digits(val):
    num_digit = 0
    while val > 0:
        num_digit += 1
        val = floor(val / 10)
    return num_digit


def get_max_digits(arr):

    """Find the maximum number of digits of any item"""
    digits = [get_num_digits(val) for val in arr]

    return max(digits)


def get_ith_digit(val, i):
    return floor(val / 10 ** i) % 10


def radix_sort(arr: List[CT]) -> List[CT]:
    # loop from the right-most digit to the highest digit
    for i in range(get_max_digits(arr)):
        # initialize buckets for base 10 numbers
        buckets = [[] for _ in range(10)]
        # for each place, we're sorting by the digit value
        # as we go up in places, all the values less than the current place are already sorted among themselves
        for val in arr:
            ith_digit = get_ith_digit(val, i)
            buckets[ith_digit].append(val)
        arr = flatten(buckets)
    return arr


"""
[111, 15, 22242, 84, 3, 0, 65]
i=0, [[0], [111], [22242], [3], [84], [15, 65], [], [], [],..]
[0, 111, 22242, 3, 84, 15, 65]
i=1, [[0, 3], [111, 15], [], [3], [22242], [], [65], [], [84], [], []]
[0, 3, 111, 15, 22242, 65, 84]
i=2, [[0, 3, 15, 65, 84], [111], [22242], [], [], ...]
[0, 3, 15, 65, 84, 111, 22242]
i=3, [[0, 3, 15, 65, 84, 111], [22242], [], ...]
i=4,
i=5, [[0, 3, 15, 65, 84, 111, 22242], [], ...]
"""

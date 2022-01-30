from typing import Any, List, Union


def sum_zero(integers: List[int]) -> Union[List[int], None]:
    i = 0
    j = len(integers) - 1
    while i < j and i <= 0 and j >= 0:
        sum = integers[i] + integers[j]
        if sum < 0:
            i += 1
        elif sum > 0:
            j -= 1
        else:
            return [integers[i], integers[j]]
    return None


def count_unique_values(sorted_ints: List[int]) -> int:
    if len(sorted_ints) == 0:
        return 0
    # If there is at least one item in the list, it should count as a unique value
    count = 1
    i = 0
    j = 1
    while j < len(sorted_ints):
        if sorted_ints[i] == sorted_ints[j]:
            j += 1
        # advance j until it points to a different integer
        else:
            count += 1
            i = j  # reset i to that new integer to compare the future values
            j += 1  # and advance j
    return count


# [1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]
#                    i
#                    j


def are_there_duplicates(*args: Any):
    sorted_args = list(args)
    sorted_args.sort()
    i = 1
    while i < len(args):
        if sorted_args[i - 1] == sorted_args[i]:
            return True
        else:
            i += 1
    return False


def average_pair(sorted_ints: List[int], target_avg: float) -> bool:
    if len(sorted_ints) < 2:
        return False
    i = 0
    j = len(sorted_ints) - 1
    while i < j:
        avg = (sorted_ints[i] + sorted_ints[j]) / 2
        if avg > target_avg:
            j -= 1
        elif avg < target_avg:
            i += 1
        else:
            return True
    return False


def is_subsequence(str1: str, str2: str) -> bool:
    index1 = 0
    index2 = 0
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] == str2[index2]:
            index1 += 1
            index2 += 1
        else:
            index2 += 1
    # we found all characters in str1 in str2
    return index1 == len(str1)

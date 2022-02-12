import math
from typing import Any, List, TypeVar
from abc import ABCMeta, abstractmethod


# https://stackoverflow.com/a/37669538
class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)


def linear_search(arr: List[Any], target: Any) -> int:
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1


def binary_search(arr: List[CT], target: CT) -> int:
    head = 0
    tail = len(arr) - 1
    while head <= tail:
        mid = math.floor(tail - head / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            head = mid + 1
        elif target < arr[mid]:
            tail = mid - 1
    return -1


def naive_string_search(source: str, sub_str: str) -> int:
    count = 0

    for i, char in enumerate(source):
        if char == sub_str[0]:
            match = True
            for j, sub_char in enumerate(sub_str):
                if sub_char != source[i + j]:
                    match = False
            if match:
                count += 1
    return count

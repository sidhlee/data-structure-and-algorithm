from abc import ABCMeta, abstractmethod
from typing import Any, List, TypeVar


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)


def swap(arr: List[Any], index1: int, index2: int):
    pass


def bubble_sort(arr: List[CT]) -> List[CT]:
    return []


def selection_sort(arr: List[CT]) -> List[CT]:
    return []


def insertion_sort(arr: List[CT]) -> List[CT]:
    return []


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

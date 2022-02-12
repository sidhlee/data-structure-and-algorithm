from typing import Any, List, TypeVar
from abc import ABCMeta, abstractmethod


# https://stackoverflow.com/a/37669538
class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)


def linear_search(arr: List[Any], item: Any) -> int:
    pass


def binary_search(arr: List[CT], item: CT) -> int:
    pass


def naive_string_search(source: str, sub_str: str) -> int:
    pass

from typing import Any, Callable, List, TypeVar, Union


def collect_odd_values(numbers: List[int]) -> List[int]:
    pass


def collect_odd_values_pure(numbers: List[int]) -> List[int]:
    pass


def power(base: int, exponent: int) -> int:
    pass


def factorial(num: int) -> int:
    pass


def product_of_array(numbers: List[int]) -> int:
    pass


def sum_range(num: int) -> int:
    pass


def fib(num: int) -> int:
    pass


def reverse(string: str) -> str:
    pass


def is_palindrome(string: str) -> bool:
    pass


T = TypeVar("T")


def some_recursive(arr: List[T], cb: Callable[[T], bool]) -> bool:
    pass


def flatten_pure(arr: Union[List[T], T]) -> List[T]:
    pass


def flatten_dynamic(arr: Union[List[T], T]) -> List[T]:
    pass


def capitalize_first(arr: List[str]) -> List[str]:
    pass


def nested_even_sum(obj: Any) -> int:
    pass


def capitalize_words(words: List[str]) -> List[str]:
    pass


def stringify_numbers(obj: T) -> T:
    pass


def collect_strings(obj: Any) -> List[str]:
    pass

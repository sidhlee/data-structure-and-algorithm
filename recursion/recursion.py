from copy import deepcopy
from typing import Any, Callable, List, TypeVar, Union


def collect_odd_values(numbers: List[int]) -> List[int]:
    result = []

    def inner(index: int):
        if index == len(numbers):
            return
        if numbers[index] % 2 != 0:
            result.append(numbers[index])
        inner(index + 1)

    inner(0)
    return result


def collect_odd_values_pure(numbers: List[int]) -> List[int]:
    new_list = []
    if len(numbers) == 0:
        return []
    if numbers[0] % 2 != 0:
        new_list.append(numbers[0])
    return new_list + collect_odd_values_pure(numbers[1:])


def power(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def factorial(num: int) -> int:
    if num == 0:
        return 1
    return num * factorial(num - 1)


def product_of_array(numbers: List[int]) -> int:
    if not numbers:
        raise Exception("cannot pass an empty list")
    result = 1

    def inner(numbers):
        nonlocal result
        if not numbers:
            return
        result = result * numbers[0]
        inner(numbers[1:])

    inner(numbers)

    return result


def sum_range(num: int) -> int:
    if num == 0:
        return 0
    return num + sum_range(num - 1)


def fib(num: int) -> int:
    if num < 3:
        return 1
    return fib(num - 1) + fib(num - 2)


def reverse(string: str) -> str:
    if not string:
        return ""
    return string[len(string) - 1] + reverse(string[0:-1])


def is_palindrome(string: str) -> bool:
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return True and is_palindrome(string[1:-1])


T = TypeVar("T")


def some_recursive(arr: List[T], cb: Callable[[T], bool]) -> bool:
    if not arr:
        return False
    return cb(arr[0]) or some_recursive(arr[1:], cb)


def flatten_helper(arr: Union[List[T], T]) -> List[T]:
    result = []

    def inner(inner_array: List[T]) -> None:
        for item in inner_array:
            if isinstance(item, list):
                inner(item)
            else:
                result.append(item)

    inner(arr)

    return result


def flatten_pure(arr: Union[List[T], T]) -> List[T]:
    if not isinstance(arr, list):
        return [arr]
    if len(arr) == 0:
        return []
    # python also returns an empty list when slicing from index out of range
    return flatten_pure(arr[0]) + flatten_pure(arr[1:])


def capitalize_first(arr: List[str]) -> List[str]:
    result = []

    def inner(arr: List[str]) -> None:
        if not arr:
            return
        first_item = arr[0]
        capitalized_first_item = first_item[0].upper() + first_item[1:]
        result.append(capitalized_first_item)
        inner(arr[1:])

    inner(arr)
    return result


def nested_even_sum(obj: dict) -> int:
    sum = 0

    def inner(obj: dict) -> None:
        if not obj:
            return
        nonlocal sum
        for _, value in obj.items():
            if isinstance(value, int) and value % 2 == 0:
                sum += value
            elif isinstance(value, dict):
                inner(value)

    inner(obj)

    return sum


def capitalize_words(words: List[str]) -> List[str]:
    result = []

    def inner(words: List[str]) -> None:
        if not words:
            return
        first_word = words[0]
        capitalized = first_word.upper()
        result.append(capitalized)
        inner(words[1:])

    inner(words)

    return result


def stringify_numbers(obj: dict) -> dict:
    copied_obj = deepcopy(obj)

    def inner(obj: dict) -> None:
        if not obj:
            return
        for key, value in obj.items():
            # bool is subclass of int in python
            if isinstance(value, bool):
                continue
            elif isinstance(value, int):
                obj[key] = str(value)
            elif isinstance(value, dict):
                inner(value)

    inner(copied_obj)

    return copied_obj


def collect_strings(obj: Any) -> List[str]:
    result = []

    def inner(obj: dict):
        if not obj:
            return
        for _, val in obj.items():
            if isinstance(val, str):
                result.append(val)
            elif isinstance(val, dict):
                inner(val)

    inner(obj)

    return result

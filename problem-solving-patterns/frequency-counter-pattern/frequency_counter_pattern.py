from typing import Any, Dict, List, Union
from collections import deque
import math


def same_naive(arr1: List[int], arr2: List[int]) -> bool:
    """O(n^2) implementation"""
    if len(arr1) != len(arr2):
        return False
    arr2_copy = arr2.copy()  # don't mutate the input list
    for item in arr1:
        try:
            # removes item from arr2 with O(n)
            arr2_copy.remove(item ** 2)
        except ValueError:
            # item doesn't exist in arr2
            return False
    return True


def same(arr1: List[int], arr2: List[int]) -> bool:
    """O(n) using hashmap to comapre the two lists"""
    dict_1 = get_frequency_dict(arr1)
    dict_2 = get_frequency_dict(arr2)
    if len(dict_1) != len(dict_2):
        return False
    for item in dict_1:
        try:
            # Python raises KeyError if key is not found in dict
            # and it can have any type as the key so we can do math ops directly
            if dict_1[item] != dict_2[item ** 2]:
                return False
        except KeyError:  # if the item doesn't exist in dict_2
            return False
    return True


def get_frequency_dict(list: List[Union[str, int]]):
    frequency_dict = {}
    for item in list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict


def is_anagram(str1: str, str2: str) -> bool:
    """Determines if two strings are anagram

    Returns true if two empty strings are passed

    Args:
        str1 (str): First string to compare
        str2 (str): Second string to compare

    Returns:
        bool: whether or not the given strings are anagram
    """
    if len(str1) != len(str2):
        return False
    dict1 = get_frequency_dict(str1)
    dict2 = get_frequency_dict(str2)
    for letter in dict1:
        try:
            if dict1[letter] != dict2[letter]:
                return False
        except KeyError:
            return False
    return True


def same_frequency(num1: int, num2: int) -> bool:
    """Determines if two numbers have the same frequencies of digits

    eg. same_frequency(182, 281) -> True, same_frequency(24, 14) -> False

    Args:
        num1 (int): First number to compare
        num2 (int): Second number to compare

    Returns:
        bool: whether or not the given numbers have the same frequencies of digits
    """
    if get_number_of_digits(num1) != get_number_of_digits(num2):
        return False
    dict1 = get_digit_frequency_dict(num1)
    dict2 = get_digit_frequency_dict(num2)
    for digit in dict1:
        try:
            if dict1[digit] != dict2[digit]:
                return False
        except KeyError:
            return False
    return True


def get_digit_frequency_dict(num: int) -> Dict[int, int]:
    digits = num_to_digits(num)
    dict = {}
    for digit in digits:
        try:
            if dict[digit]:
                dict[digit] += 1
        except KeyError:
            dict[digit] = 1
    return dict


def num_to_digits(num: int) -> List[int]:
    # O(1) instead of O(n) using list.insert(0, val)
    # https://stackoverflow.com/a/8538295
    digits_queue = deque()

    while num > 0:
        digit = num % 10
        digits_queue.appendleft(digit)
        num = math.floor(num / 10)

    return list(digits_queue)


def get_number_of_digits(num: int) -> int:
    return math.floor(math.log10(num)) + 1


def are_there_duplicates(*args: Any) -> bool:
    dict = {}
    for arg in args:
        try:
            dict[arg] += 1
        except KeyError:
            dict[arg] = 1
    return True if any([dict[arg] > 1 for arg in args]) else False

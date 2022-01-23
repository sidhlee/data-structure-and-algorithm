from typing import List, Union


def same_naive(arr1: List[int], arr2: List[int]) -> bool:
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

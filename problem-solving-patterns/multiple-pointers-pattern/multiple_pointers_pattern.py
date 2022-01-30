from typing import List, Union


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

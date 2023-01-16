from collections import Counter


def MinWindowSubstring__fail__only_comparing_same_length(strArr):
    """
    2023-01-16 08:08:45
    This doesn't work for:
      - For input ["aaabaaddae", "aed"] the output was incorrect. The correct output is dae
    because the substring can be longer than the second string. eg. substring can include
    letters that don't belong to the substring but the letters around it do.
    """
    sub_counter = Counter(strArr[1])
    for i in range(len(strArr[0]) - len(strArr[1])):
        curr_str = strArr[0][:i]
        if not (sub_counter - Counter(curr_str)):
            for j in range(len(curr_str) - len(strArr[1])):
                if sub_counter - Counter(curr_str[j:]):
                    return curr_str[j - 1 :]


def MinWindowSubstring__fail__returns_duplicate_letters(strArr):
    """
    2023-01-16 08:56:23
    This returns multiple duplicate letters when the target is a single letter.
    We need to return the minimum substring.
    1. For input ["aaaaaaaaa", "a"] the output was incorrect. The correct output is a
    """
    sub_counter = Counter(strArr[1])
    for i in range(1, len(strArr[0]) + 1):
        curr_str = strArr[0][:i]
        if not (sub_counter - Counter(curr_str)):
            break
    for j in range(len(curr_str)):
        if sub_counter - Counter(curr_str[j:]):
            return curr_str[j - 1 :]

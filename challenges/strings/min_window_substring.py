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


def MinWindowSubstring_working_v1(strArr):
    """
    2023-01-17 06:13:33
    """
    target_counter = Counter(strArr[1])
    # Find the substring by expanding it from the beginning
    for i in range(len(strArr[0])):
        substr = strArr[0][: i + 1]
        if not (target_counter - Counter(substr)):
            break
    # Find the min window substring by shifting the head index
    for j in range(len(substr)):
        # when the substring begins to not cover the target, return the prev string
        if target_counter - Counter(substr[j:]):
            return substr[j - 1 :]
    # when target is a single letter we never get into the if block above
    return substr


def MinWindowSubstring_readable(strArr):
    """
    2023-01-17 06:52:43
    """
    master, target = strArr
    target_counter = Counter(target)
    for i in range(len(master)):
        substr = master[: i + 1]
        substr_includes_target = not target_counter - Counter(substr)
        if substr_includes_target:
            break
    for j in range(len(substr)):
        min_win_substr = substr[j:]
        min_win_substr_includes_target = not target_counter - Counter(min_win_substr)
        if not min_win_substr_includes_target:
            return substr[j - 1 :]
    return min_win_substr


MinWindowSubstring = MinWindowSubstring_readable

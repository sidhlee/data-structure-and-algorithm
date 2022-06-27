"""
["flower","flow","flight"] -> "fl
["cir", "car"] -> "c"
["ab", "a"] -> "a"
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Runtime: 42 ms (76%)
        Memory Usage: 14 MB (0%)
        """
        if len(strs) < 2:
            return strs[0]
        prefix = ""
        strs.sort(key=len)
        for i, c in enumerate(strs[0]):
            if all([str[i] == c for str in strs[1:]]):
                prefix += c
            else:
                break
        return prefix

    def longestCommonPrefix_no_sort(self, strs: List[str]) -> str:
        """
        2022-06-27T01:36:08.671Z
        Runtime: 37 ms (88%)
        Memory Usage: 13.9 MB (49%)
        """
        prefix = ""
        for i in range(min([len(str) for str in strs])):
            if all([str[i] == strs[0][i] for str in strs[1:]]):
                prefix += strs[0][i]
            else:
                break
        return prefix

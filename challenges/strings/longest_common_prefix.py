from typing import List

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


class Solution:
    def longestCommonPrefix_sort(self, strs: List[str]) -> str:
        """
        2022-08-24 20:51:37
        Runtime: 66 ms (25%)
        Memory Usage: 13.9 MB (50 %)

        Used sort to pick the shortest str in the list.
        slow since we're sorting the entire list first.
        """
        strs.sort(key=len)
        for i, v in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if strs[j][i] != v:
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix_return_early(self, strs: List[str]) -> str:
        """
        2022-08-24 21:27:33
        Runtime: 37 ms (91%)
        Memory Usage: 13.9 MB (50%)

        optimized to return asap
        """
        for i in range(
            len(strs[0])
        ):  # number of iteration should be no greater than the length of first string
            for j in range(1, len(strs)):
                # if we reached the end of current string or current string's ith letter doesn't match the first string's ith letter, return up to that point
                if len(strs[j]) == i or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        # if we came this far, the first string is the longest common prefix
        return strs[0]

    def longestCommonPrefix_pop(self, strs: List[str]) -> str:
        """
        2022-10-18 08:06:06

        Easier to read but mutates input array
        """
        last = strs.pop()
        for i in range(len(last)):
            for word in strs:
                if i >= len(word) or last[i] != word[i]:
                    return last[:i]
        return last

    def longestCommonPrefix_res(self, strs: List[str]) -> str:
        """
        2022-12-29 12:00:02
        """
        res = ""
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return res
            res += c
        return res

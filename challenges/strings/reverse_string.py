"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""

from typing import List


class Solution:
    def reverseString_swap(self, s: List[str]) -> None:
        """
        2022-06-25T22:18:53.379Z
        Runtime: 314 ms (39%)
        Memory Usage: 18.3 MB (87%)

        without using s.reverse()
        """
        for i in range(len(s) // 2):
            t = s[i]
            s[i] = s[~i]
            s[~i] = t

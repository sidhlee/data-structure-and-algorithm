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

    def reverseString_two_pointers(self, s: List[str]) -> None:
        """
        2022-08-20 20:09:11
        Runtime: 209 ms (92%)
        Memory Usage: 18.3 MB (86%)

        more readable
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def reverseString_tilde_swap(self, s: List[str]) -> None:
        """
        2022-10-16 16:35:26
        ~0 == -1, ~1 == -2

        when i = 3,
        3 -> 0000 0011
        ~3 -> 1111 1100 -> -4
        -3 -> 1111 1101 (2's complement - we find the complements of 1s and add 1)

        Why do we add 1 in 2's complement: because of 0
        0 -> 0000 0000
        ~0 -> 1111 1111
        1111 1111 + 1 = 1 0000 0000 -> 0000 0000 (1 is shifted out of the 8-bit range)
        By adding 1 to the 2's complement, we can get 0 instead of -0

        ~0 + 1 = 1111 1111 + 1 = 0000 0000 = 0 -> ~0 = 0 - 1
        ~1 + 1 = 1111 1110 + 1 = 1111 1111 = -1 -> ~1 = -1 - 1
        ~2 + 1 = 1111 1101 + 1 = 1111 1110 = -2 -> ~2 = -2 - 1

        2's complement is used to represent negative numbers in binary
        because we can use the same addition and subtraction operations for both positive and negative numbers

        1 -> 0000 0001
        ~1 -> 1111 1110
        1111 1110 + 1 = 1111 1111 -> -1

        """
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]

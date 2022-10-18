"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        2022-06-27T00:42:21.134Z
        Runtime: 29 ms (95%)
        Memory Usage: 13.9 MB (15%)
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

    def strStr_one_line(self, haystack: str, needle: str) -> int:
        '''
        2022-08-24 08:34:42
        Runtime: 30 ms (95%)
        Memory Usage: 13.8 MB (65%)
        '''
        return haystack.find(needle)

    def strStr_optimized(self, haystack: str, needle: str) -> int:
        '''
        2022-10-18 07:47:27
        will only compare if the first letter matches
        '''
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0] and haystack[i:i + len(needle)] == needle:
                return i
        return -1

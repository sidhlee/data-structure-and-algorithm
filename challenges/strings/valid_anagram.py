"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

from collections import Counter


class Solution:
    def isAnagram_counter(self, s: str, t: str) -> bool:
        """
        2022-06-26T02:25:33.257Z
        Runtime: 40 ms (98%)
        Memory Usage: 14.5 MB (34%)

        Python counters are comparable by values.
        """
        return Counter(s) == Counter(t)

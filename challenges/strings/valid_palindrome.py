"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

import math


class Solution:
    def isPalindrome_two_pointers(self, s: str) -> bool:
        """
        2022-06-26T02:44:57.775Z
        Runtime: 68 ms (57%)
        Memory Usage: 14.4 MB (86%)

        use two pointers and return early
        """
        an = "qazwsxedcrfvtgbyhnujmikolp1234567890"
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in an:
                i += 1
                continue
            else:
                if s[j] not in an:
                    j -= 1
                    continue
                else:
                    if s[i] == s[j]:
                        i += 1
                        j -= 1
                    else:
                        return False
        return True

    def isPalindrome_use_memory(self, s: str) -> bool:
        """
        2022-06-26T21:25:11.846Z
        Runtime: 55 ms (80%)
        Memory Usage: 19.2 MB (9%)

        Filter only alpha-numeric from the string and map them to lowercase.
        Compare the first half with the second half using slicing
        """
        s = "".join([x.lower() for x in s if x.isalnum()])
        return s[: len(s) // 2] == s[: math.ceil(len(s) / 2) - 1 : -1]

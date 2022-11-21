"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

from collections import Counter


class Solution:
    def firstUniqChar_dict(self, s: str) -> int:
        """
        2022-06-25T23:21:35.840Z
        Runtime: 123 ms (76%)
        Memory Usage: 15.6 MB (0%)

        using dict to avoid O(n^2) for lookup.
        """
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [i]
            else:
                d[c].append(i)
        for v in d.values():
            if len(v) == 1:
                return v[0]

        return -1

    def firstUniqChar_counter(self, s: str) -> int:
        """
        2022-06-26T02:18:41.272Z
        Runtime: 158 ms (55%)
        Memory Usage: 14.1 MB (97%)

        If we're not returning early (i.e. we have to finish looping at least once),
        we don't need to manually save it to the dict.
        Instead, we can turn them into a counter.

        Also, we don't care about the indices of the duplicates. We just need to check
        if the character shows up more than once. so appending index to the list is not necessary.

        We return the index from the original string, so it make sense to iterate
        through the original string and stop where the counter has the only one occurrence.
        -> we're still returning early so it's <= O(2n)

        * counter doesn't guarantee the element order

        2022-08-21 08:39:48
        We need to iterate through the entire string at least once.
        -> create a counter and return when curr character count is 1 (return early)
        """
        c = Counter(s)
        for i in range(len(s)):  # could use enumerate
            if c[s[i]] == 1:
                return i
        return -1

    def firstUniqChar_use_dict(self, s: str) -> int:
        """
        2022-10-17 05:41:07
        Runtime: 212 ms (53%)
        Memory Usage: 14 MB (95%)

        manually creates a dict with all unique characters and their indices.

        Dictionary:
        1. create a dict - loop through the string and manually populate letters with index: O(n)
        2. create dict_values object and loop through to find non-repeating index
        -> O(2n) + 2 objects created
        * Converting objects cost space!

        Counter:
        1. create a counter O(n)
        2. loop through the given string: O(n)
            - Find the letter from the counter and check if the value is 1: O(1)
            - If the value is 1, return the string index
        -> O(2n) + 1 object created
        """
        chars = {}
        # here, we need to loop entire string to find out about the duplication
        for i, char in enumerate(s):
            if char in chars:
                chars[char] = -1
            else:
                chars[char] = i
        # we can return as soon as find non repeating character
        for i in chars.values():
            if i != -1:
                return i
        return -1

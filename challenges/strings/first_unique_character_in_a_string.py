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

        If we're not returning early, we don't need to manually save it to the dict.
        Instead, we can turn them into a counter.

        Also, we don't care about the indices of the duplicates. We just need to check
        if the character shows up more than once. so appending index to the list is not necessary.

        We returning the index from the original string, so it make sense to iterate
        through the original string and stop where the counter has the only one occurrence.

        * counter doesn't guarantee the element order
        """
        c = Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1

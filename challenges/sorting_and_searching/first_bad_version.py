"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1

Constraints:

1 <= bad <= n <= 2^31 - 1
"""


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        2022-07-17 11:09:30
        Runtime: 58 ms (44%)
        Memory Usage: 13.9 MB (97%)

        Look left every time the mid is bad. If left is good, return mid.
        Slow because of extra API call when mid is bad.
        eg. if the first version is bad, will make 2 * log(n) calls

        looks like other solutions are utilizing caching (slow time, great space)
        """
        left, right = 1, n
        mid = (left + right) // 2
        last_moved = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                if mid == last_moved:
                    return mid
                right = mid - 1
                if not isBadVersion(right):
                    return mid
                else:
                    last_moved = right
            else:
                left = mid + 1
                last_moved = left
        return last_moved

    def firstBadVersion_keep_latest_bad_on_right(self, n: int) -> int:
        """
        Runtime: 28 ms (96%)
        Memory Usage: 13.7 MB (97%)

        move the right pointer to include the latest bad version.
        when we get out of the loop, it's either:
        1. right comes to the left
            - mid was bad
            - right comes to mid and mid was at the left
              - mid is left when left and right are next to each other
            - eg. [1, 2] bad = 1, 2
        2. left comes to the right
            - mid was good
            - right was at mid + 1
            - eg. [1, 2] bad = 2

        What if left is bad at the beginning?
        -> range keeps being reduced in half until right comes to left (case 1)

        TLDR;
        - Keep target included in the range while narrowing it down.
        - When the left and right meet, it should still include the target.
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right

    def firstBadVersion_better_naming(self, n: int) -> int:
        '''
        2023-01-05 06:14:48
        '''
        mn_first_bad, mx_first_bad = 1, n
        while mn_first_bad < mx_first_bad:
            mid = (mn_first_bad + mx_first_bad) // 2
            if isBadVersion(mid):
                # mid can be the first bad version, but we don't know.
                # all we know is that we don't need to look at versions after this.
                mx_first_bad = mid
            else:
                # curr mid is good. first bad could be the next one.
                mn_first_bad = mid + 1
        return mx_first_bad
"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct. 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def containsDuplicate_set(self, nums: List[int]) -> bool:
        """
        Runtime: 469 ms (93%)
        Memory Usage: 25.9 MB (72%)

        return early if you can by checking inside the loop
        """
        s = set()
        i = 0
        for n in nums:
            s.add(n)
            i += 1
            if len(s) != i:
                return True
        return False

    def containsDuplicate_less_line(self, nums: List[int]) -> bool:
        """
        2022-06-23T11:22:16.538Z
        Runtime: 460 ms (96%)
        Memory Usage: 26 MB (30%)

        reduces one line in the loop by using enumerate
        """
        s = set()
        for i, n in enumerate(nums):
            s.add(n)
            if len(s) != i + 1:
                return True
        return False

    def containsDuplicate_one_line(self, nums: List[int]) -> bool:
        """
        2022-08-14 19:54:21
        Runtime: 521 ms (80%)
        Memory Usage: 26.1 MB (31%)

        uses the least amount lines
        """
        return len(set(nums)) != len(nums)

    def containsDuplicate_return_early(self, nums: List[int]) -> bool:
        """
        2023-05-17 06:45:35
        return early if already found.
        """
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

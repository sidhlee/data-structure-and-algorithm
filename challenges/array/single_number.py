from typing import List

"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

"""


class Solution:
    def singleNumber_inplace_reduction(self, nums: List[int]) -> int:
        """
        2022-06-14T12:42:37.741Z
        Runtime: 1342 ms (p15.01)
        Memory Usage: 15.8 MB (p99.78)

        remove inside for loop might still lead to O(n^2), but nums get smaller in each loop
        so amortized time seems to be better than expected
        """
        for i in range(len(nums), 0, -1):
            num = nums.pop()
            try:
                nums.remove(num)
            except Exception:
                return num

    def singleNumber_math(self, nums: List[int]) -> int:
        """
        2022-06-14T12:50:27.938Z
        Runtime: 123 ms (99.77%)
        Memory Usage: 17.2 MB (0%)

        If there is very specific constraints we can take advantage, try using math.
        This solution is not O(1) space though.
        """
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumber_xor(self, nums: List[int]) -> int:
        """
        2022-06-24T11:45:05.886Z
        Runtime: 152 ms (79%)
        Memory Usage: 16.9 MB (20%)

        Used XOR properties to cancel out all the duplicated numbers
        Linear and no extra memory used.
        Also returns early for len(nums) < 2.
        """
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

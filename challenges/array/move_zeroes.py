"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/567/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Do not return anything, modify nums in-place instead.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

from typing import List


class Solution:
    def moveZeroes_slicing_inside_loop(self, nums: List[int]) -> None:
        """
        2022-06-17T12:28:51.268Z
        Runtime: 1444 ms (7%) -> truncating decimals because leetcode distribution is flaky so the accuracy is not that meaningful
        Memory Usage: 15.6 MB (64%)

        Using list slicing, but slow because it's O(n^2)
        """
        j = 0
        for _ in range(len(nums)):
            if nums[j] == 0:
                nums[j:] = nums[j + 1 :] + [0]
            else:
                j += 1

    def moveZeroes_fill_zeroes_after_loop(self, nums: List[int]) -> None:
        """
        2022-06-17T12:45:02.925Z
        Runtime: 264 ms (44%)
        Memory Usage: 15.5 MB (97%)

        Because the thing we're moving to the back of the list is always same value (0),
        we can move only one number inside the loop O(n)
        and fill all the zeros outside the loop O(1)
        """
        j = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[j] = n
                j += 1
        nums[j:] = [0] * (len(nums) - j)

    def moveZeroes_fill_zeroes_after_loop_opt(self, nums: List[int]) -> None:
        """
        2022-06-17T12:45:02.925Z
        Runtime: 157 ms (99%)
        Memory Usage: 15.5 MB (64%)

        adds a check to skip copying the number if there are many non-zeroes at the beginning
        """
        j = 0
        for i, n in enumerate(nums):
            if n != 0:
                if i != j:
                    nums[j] = n
                j += 1
        nums[j:] = [0] * (len(nums) - j)

    def moveZeroes_access_with_index(self, nums: List[int]) -> None:
        """
        2022-06-25T15:38:10.158Z
        Runtime: 219 ms (67%)
        Memory Usage: 15.5 MB (65%)

        If you're going to access the array item more than once, enumerate is better
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                if i != j:
                    nums[i] = nums[j]
                i += 1
        nums[i:] = [0] * (len(nums) - i)

    def moveZeroes_no_extra_space(self, nums: List[int]) -> None:
        """
        2022-08-17 08:25:37
        Runtime: 177 ms (91%)
        Memory Usage: 15.6 MB (66%)

        creating a list with a zero then multiplying it costs O(m) space where m is the number of zeroes.
        Using another for loop gives us constant space with O(2n) time.
        """
        insert_at = 0
        for v in nums:
            if v != 0:
                nums[insert_at] = v
                insert_at += 1
        for i in range(insert_at, len(nums)):
            nums[i] = 0

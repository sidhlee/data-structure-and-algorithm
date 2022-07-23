from typing import List

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


class Solution:
    def rob_look_back(self, nums: List[int]) -> int:
        """
        2022-07-23 14:08:40
        Runtime: 41 ms (72%)
        Memory Usage: 13.8 MB (66%)

        Finding max or min -> iterate while updating (dynamic programming)
        1. If the max two steps before the current number + current number > the max one step before
            -> update the max with the sum
        2. else (if the max one step before is still greater than or equal to the current number + max two steps away)
            -> keep the max one step away as the max and update the max two steps away
            with the max one step away so that you can use it in the next iteration
            * In the next iteration, max two step away is the same as max one step away
            eg. [2, 1, 1, 2]

        """
        mx_one_before = nums[0]
        mx_two_before = 0
        for i in range(1, len(nums)):
            curr_num = nums[i]
            if mx_two_before + curr_num > mx_one_before:
                temp = mx_one_before
                mx_one_before = mx_two_before + curr_num
                mx_two_before = temp
            else:
                mx_two_before = mx_one_before
        return mx_one_before

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

        This seems to be more complicated compared to the bottom-up approach
        """
        mx_one_before = nums[0]
        mx_two_before = 0
        for i in range(1, len(nums)):
            # starting from the second house
            curr_num = nums[i]
            if mx_two_before + curr_num > mx_one_before:
                temp = mx_one_before
                mx_one_before = mx_two_before + curr_num
                mx_two_before = temp
            else:
                mx_two_before = mx_one_before
        return mx_one_before

    def rob_look_behind_easier(self, nums: List[int]) -> int:
        """
        2022-11-09 06:54:47

        Get the max profit at the current house by comparing max profit upto the second and third last house.
        Update overall max profit with the current max profit if it's greater than max profit up to the last house
        """
        max_profit = nums[0]
        mp_upto_last = nums[0]
        mp_upto_second_last = 0
        mp_upto_third_last = 0
        for i in range(1, len(nums)):
            curr_mp = max(mp_upto_second_last + nums[i], mp_upto_third_last + nums[i])
            max_profit = max(curr_mp, mp_upto_last)

            # Advance pointers
            mp_upto_third_last = mp_upto_second_last
            mp_upto_second_last = mp_upto_last
            mp_upto_last = curr_mp
        return max_profit

    def rob_bottom_up(self, nums: List[int]) -> int:
        """
        2022-09-25 16:16:54
        Runtime: 38 ms (84%)
        Memory Usage: 13.8 MB (97%)

        Assumptions:
        - either the last or second last house is robbed
        - either we skip 1 house or 2 houses to make max profit
        - either we start from first or second house

        Start looping from the last house, and keep updating the cache with
        the sum of the current value and the the value of i + 2 or i + 3 whichever is greater.
        1. Store the index:value pair to the cache.
        2. If index + 2 exists in cache, store the sum of current value and the value of index + 2
        3. If index + 3 exists in cache, store the sum of current value and the max between i + 2 or i + 3
        4. After the loop is done, return the bigger value from i or i + 1 from the cache

        - The max profit from the current house is the value of the current house
        added by the profit I'll make from the next house, which can be i + 2, or i + 3.

        [2, 1, 1, 2]
        skip is either 1 or 2.
        no need to skip more than 3: robbing house in the middle for more profit
        can start from i = 0 or 1
        2 -> 1
        2 -> 2
        [5, 10, 2, 1, 10, 5]
                   ------>
                   --------->
                ------>
                ---------->
            ------->
            --------->10
         ------>
         ---------->

        5 > 2 > 10
        5 > 2 > 5
        5 > 1 > 5
        10 > 10
        10 > 1 > 5
        """
        profits = {}
        for i in range(len(nums) - 1, -1, -1):
            profits[i] = nums[i]
            if i + 2 in profits:
                profits[i] = nums[i] + profits[i + 2]
            if i + 3 in profits:
                profits[i] = nums[i] + max(profits[i + 2], profits[i + 3])
        return max(profits[0], profits[1]) if profits.get(1) else profits[0]

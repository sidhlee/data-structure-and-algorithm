from typing import List

"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array. 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray_add_and_remove(self, nums: List[int]) -> int:
        """
        2022-07-21 08:34:29
        Runtime: 1152 ms (42%)
        Memory Usage: 27.7 MB (98%)

        Loop through the list adding each number to the sum
        if the sum <= 0, subarray up to that point doesn't contribute to the max.
        - subtract that part
        """
        mx = subsum = left = 0
        for right in range(len(nums)):
            subsum += nums[right]
            if subsum <= 0:
                subsum -= sum(nums[left : right + 1])
                left = right + 1
            else:
                mx = max(mx, subsum)
        if mx <= 0:
            return max(nums)
        return mx

    def maxSubArray_add_and_reset(self, nums: List[int]) -> int:
        """
        Runtime: 721 ms (97%)
        Memory Usage: 28.4 MB (16%)

        - set the first value as max and keep accumulating numbers
        - if the accumulation becomes larger than the max, update max
        - but if that accumulation is not positive, reset it to 0 (not contributing to max)
        - continue accumulating the next number to the sum (updated or not)
        - if the sum becomes larger than the max, update it again
        """
        max_sub, sum_sub = nums[0], 0
        for num in nums:
            sum_sub += num
            # first number never get into this block
            # then every time sum gets larger than the max, we update the max
            if sum_sub > max_sub:
                max_sub = sum_sub
            # if sum gets below zero, we reset sum to zero
            # this has to check after the first one
            # otherwise, [-1] would reset sum to 0 and it becomes larger than the max
            if sum_sub <= 0:
                sum_sub = 0
            # we can get into both blocks for [-2, 1 ]:
            # - second number is positive
            # - but the sum of first and second numbers is less than 0

            # We get into only the first condition for [-2, 3]
            # - num is positive, so sum increased
            # - sum is positive, so keep the current sum

            # We get into only the second condition for [-2, 0]
            # - sum stays at the first number, -2, which is also the max
            # - sum is negative, so we reset it to 0

            # we don't get into either for [2, -1]
            # - sum is decreased by negative num
            # - but the sum is still positive, so keep the sum
        return max_sub

    def maxSubArray_reset_and_add(self, nums: List[int]) -> int:
        '''
        2022-09-25 12:53:17
        Runtime: 844 ms (83%)
        Memory Usage: 27.8 MB (96%)
        1. Init: 
        - set the max_sum with the first number
        - set the current sum to 0
        2. loop through the numbers
            a. reset curr_sum to 0 if negative. This is the same resetting
            subarray head to the current number since the part coming before is not
            contributing to the max sum
            b. add current number to the curr_sum
            c. If the updated curr_sum is greater than max_sum, we update max_sum.
            max_sum will NOT update if the curr_sum is equal to the max_sum.
        This works for:
        - single negative number
        - all negative numbers
        
        You can also update max_sum only if curr_sum is greater than curr_sum,
        then reset the curr_sum if less than zero.
        This works if there's one negative number
        ''' 
        max_sum = nums[0]
        curr_sum = 0
        for i in range(len(nums)):
            # check current sum and reset to 0 if negative before adding the current number
            curr_sum = max(0, curr_sum)
            # adding the current number after reset will work for single negative number and all neggative numbers
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)     
        return max_sum
            

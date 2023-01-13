from typing import List

"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.


Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""


class Solution:
    def missingNumber_combined_logic(self, nums: List[int]) -> int:
        """
        Runtime: 141 ms (93%)
        Memory Usage: 15.3 MB (35%)

        Uses len(nums) instead of n so that when there is zero in the list,
        we get the n + 1 as the missing number.
        When there is no zero in the list, 
        we'll get zero as the missing number.
        
        len(nums) == max_num except when the missing number is max_num + 1
        -> By using len(nums) to calculate sum of the sequence and finding the difference from sum(nums)
           we can get the missing number in all scenarios
        """
        return int(len(nums) * (len(nums) + 1) / 2) - sum(nums)
    
    def missingNumber_separate_logic(self, nums: List[int]) -> int:
        '''
        2022-10-11 08:37:57
        Runtime: 159 ms (85%)
        Memory Usage: 15.3 MB (21%) 
        
        Uses iteration to find the max number and if zero is included in the list.
        Easier to understand
        
        [0] -> 1
        [1] -> 0 (only case when there's no 0)
        [0, 2] -> 1
        [0, 1] -> 2
        [0, 3, 2] -> 1 
        
        numbers are not ordered
        there is maximum 1 missing number
        0 + 1 + 2 + 3 + 4 + 5 = (1 + 5) * 5 / 2 = 15
        0 + 1 + 2 + 3 + 4 = (1 + 4) * 4 / 2 = 10
        (min + max) * 
        
        2022-12-20 06:44:12
        This is wasteful because we know that the numbers are sequential **regardless of their order**.
        -> If len(nums) == 5, we know that there is one number that completes the sequence
        -> we can use the math to find the sum of the sequence then loop through the array to find the actual sum
        - 0, 1, 2, 3, 4 -> 5
        - 1, 2, 3, 4, 5 -> 0
        - 0, 1, 2, 4, 5 -> 3
    
        '''
        total = mx = 0
        has_zero = False
        for num in nums:
            total += num
            mx = max(mx, num)
            has_zero = has_zero or num == 0
        diff = int((1 + mx) * mx / 2) - total
        if not has_zero:
            return 0
        return mx + 1 if diff == 0 else diff

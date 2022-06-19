"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/546/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List


class Solution:
    def twoSum_bad_but_works(self, nums: List[int], target: int) -> List[int]:
        """
        2022-06-19T15:24:08.426Z
        Runtime: 8938 ms (0%)
        Memory Usage: 17.3 MB (0%)

        This one barely passes the time limit 🥲
        Still O(n^2) but inner loop becomes smaller and smaller
        """
        nums[:] = [{"i": i, "v": v} for (i, v) in enumerate(nums)]
        nums.sort(key=lambda d: d["v"])

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i]["v"] + nums[j]["v"] == target:
                    return [nums[i]["i"], nums[j]["i"]]

    def twoSum_lookup_visited(self, nums: List[int], target: int) -> List[int]:
        """
        2022-06-19T15:47:42.063Z
        Runtime: 103 ms (54%)
        Memory Usage: 15.2 MB (50%)

        When the size of the input array can go up to orders of billions,
        and the brute force solution involves nested loop (O(n^2)),
        consider saving the current value into hashmap while looping and take advantage of O(1) lookup.
        """
        visited = {}
        for i, n in enumerate(nums):
            other_num = target - n
            if other_num in visited:
                # visited number index is always lower than i
                return [visited[other_num], i]
            else:
                visited[n] = i

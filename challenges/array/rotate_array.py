"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Do not return anything, modify nums in-place instead.

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Hint #1
The easiest solution would use additional memory and that is perfectly fine.

Hint #2
The actual trick comes when trying to solve this problem without using any additional memory.
This means you need to use the original array somehow to move the elements around. 
Now, we can place each element in its original location and shift all the elements around it
to adjust as that would be too costly and most likely will time out on larger input arrays.

Hint #3
One line of thought is based on reversing the array (or parts of it) to obtain the desired result. 
Think about how reversal might potentially help us out by using an example.

Hint #4
The other line of thought is a tad bit complicated but essentially it builds on the idea of placing
each element in its original position while keeping track of the element originally in that position.
Basically, at every step, we place an element in its rightful position and keep track of the element
already there or the one being overwritten in an additional variable. 
We can't do this in one linear pass and the idea here is based on cyclic-dependencies between elements.
"""

from typing import List


class Solution:
    def rotate_by_slicing(self, nums: List[int], k: int) -> None:
        """
        Runtime: 325 ms (54%)
        Memory Usage: 25.4 MB (75%)
        """
        k %= len(nums)
        if k != 0:
            nums[:] = nums[-k:] + nums[:-k]

    def rotate_by_reverse_and_partial_reverse(self, nums: List[int], k: int) -> None:
        """
        2022-06-22T12:55:44.531Z
        Runtime: 211 ms (98%)
        Memory Usage: 25.4 MB (75%)
        """
        if len(nums) < 2:
            return
        k = k % len(nums)
        nums.reverse()
        # reversed() is faster than [::-1] because reversed() just returns an iterator
        # slicing creates a new list
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

    def rotate_without_creating_new_list(self, nums: List[int], k: int) -> None:
        """
        2022-08-14 19:39:35
        Runtime: 312 ms (67%)
        Memory Usage: 25.3 MB (76%)

        list concatenation with + creates a new list and consumes extra memory.
        Use tuple assignment to swap the front and the back of the list in place without concatenation.
        """
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[: len(nums) - k]

    def rotate_without_creating_new_list_2(self, nums: List[int], k: int) -> None:
        """
        2022-10-13 08:10:59
        Runtime: 390 ms (66%)
        Memory Usage: 25.3 MB (75%)

        Instead of using variable as the negative index
        which does't behave consistently when it's 0,
        create another variable to get the beginning index of shifting subarray
        """
        k_mod = k % len(nums)
        k_last = len(nums) - k_mod
        nums[:k_mod], nums[k_mod:] = nums[k_last:], nums[:k_last]

    def rotate_with_reverse(self, nums: List[int], k: int) -> None:
        """
        2024-02-07 06:14:32
        Runtime: 154 ms (86%)
        Memory Usage: 28 MB (75%)

        O(1) space solution

        1. reverse the whole list [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1
        2. reverse the first k elements [7,6,5,4,3,2,1] -> [5,6,7,4,3,2,1]
        3. reverse the rest of the list [5,6,7,4,3,2,1] -> [5,6,7,1,2,3,4]

        Need to return early if k is 0 after mod because of step 3 above.
        """
        k = k % len(nums)
        if k == 0:
            return

        def reverse(nums: List[int], start: int = 0, end: int = None) -> None:
            end = end or len(nums)
            for i in range((end - start) // 2):
                j = start + i
                k = end - 1 - i
                nums[j], nums[k] = nums[k], nums[j]

        reverse(nums)
        reverse(nums, 0, k)
        reverse(nums, k)

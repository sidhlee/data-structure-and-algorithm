"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

Hint #1
In this problem, the key point to focus on is the input array being sorted. As far as duplicate elements are concerned,
what is their positioning in the array when the given array is sorted? Look at the image above for the answer. 
If we know the position of one of the elements, do we also know the positioning of all the duplicate elements?
'./remove_duplicates_from_sorted_array_1.png

Hint #2
We need to modify the array in-place and the size of the final array would potentially be smaller than
the size of the input array. So, we ought to use a two-pointer approach here. 
One, that would keep track of the current element in the original array
and another one for just the unique elements.

Hint #3
Essentially, once an element is encountered, you simply need to bypass its duplicates
and move on to the next unique element.

"""

from typing import List


class Solution:
    def removeDuplicates_first_try(self, nums: List[int]) -> int:
        """
        Runtime: 106 ms (75%)
        Memory Usage: 15.6 MB (60%)
        """
        if len(nums) <= 0:
            return 0

        curr_insert_at = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[curr_insert_at] = nums[i]
                curr_insert_at += 1

        return curr_insert_at

    def removeDuplicates_pop(self, nums: List[int]) -> int:
        """
        2022-06-21T10:17:24.654Z
        Runtime: 154 ms (38%)
        Memory Usage: 15.6 MB (60%)

        we're shifting the subarray after the element that was just popped.
        -> O(n^2)
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
        return len(nums)

    def removeDuplicates_two_pointers(self, nums: List[int]) -> int:
        """
        2022-06-21T10:43:36.739Z
        Runtime: 95 ms (87%)
        Memory Usage: 15.5 MB (60%)

        advance i if the number at i is equal to the number at k
        if not, only copy the number at i to the right of k if they're not already adjacent.
        advance k over to the newly copied number.
        """
        k = 0
        i = 1
        while i < len(nums):
            if nums[k] == nums[i]:
                i += 1
            else:
                if i != k + 1:
                    nums[k + 1] = nums[i]
                k += 1
        return k + 1

    def removeDuplicates_curr_unique_num(self, nums: List[int]) -> int:
        """
        2022-08-06 09:30:07
        Runtime: 86 ms (97%)
        Memory Usage: 15.5 MB (61%)

        We keep:
        - index to copy unique numbers onto
        - curr_unique_num to compare current number

        Improvements:
        - for loop reduces 1 line for incrementing when using while loop
        - only one index pointer and using var to store temp values for comparison
            -> removes one condition block
            -> much simpler (we need to just check if they'are duplicated. so just store value to compare, not the index of the duplicate number)
        """
        i_copy = 1
        curr_unique_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != curr_unique_num:
                nums[i_copy] = curr_unique_num = nums[i]
                i_copy += 1
        return i_copy

    def removeDuplicates_check_behind_insert_at(self, nums: List[int]) -> int:
        """
        2022-10-12 08:15:05
        Runtime: 135 ms (75%)
        Memory Usage: 15.6 MB (66%)

        Check the insert_at - 1 for the last inserted number to compare
        This will run O(n) on the sorted unique numbers, but we need O(n) for checking all list items anyways
        and mutating list item is cheap.
        """
        insert_at = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[insert_at - 1]:
                nums[insert_at] = nums[i]
                insert_at += 1
        return insert_at

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        2022-11-19 20:40:22
        keep track of the min value to compare against instead of the inserting position.
        We're always inserting to the right of the comparing number
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[j] > nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1

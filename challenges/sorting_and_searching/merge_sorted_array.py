from typing import List

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

Follow up: Can you come up with an algorithm that runs in O(m + n) time?

Hint #1  
You can easily solve this problem if you simply think about two elements at a time
rather than two arrays. We know that each of the individual arrays is sorted.
What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?

Hint #2  
If you simply consider one element each at a time from the two arrays
and make a decision and proceed accordingly, you will arrive at the optimal solution.
"""


class Solution:
    def merge_two_pointers(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        2022-07-15 07:29:40
        Runtime: 58 ms (49%)
        Memory Usage: 13.9 MB (86%)

        First attempt & works -> room for improvement
        - both arrays are already sorted
        - optimize by comparing last non-empty value from nums1 and first value from nums2
        - It's O(n^2) due to insert. -> can we not do this? in-place slicing?
        """
        if n == 0:
            return
        p2 = p1 = 0
        for i in range(m + n):  # takes m + n times for [1, 2, 0, 0] 2 [3, 4] 2
            if p2 == n:  # when p2 goes out of nums2, means it's done
                break
            n1, n2 = nums1[p1], nums2[p2]
            # when p1 is not the padding value -> could save iteration by just slicing
            if p1 < m + p2 and n1 <= n2:
                p1 += 1
            else:
                # when p1 reached the padding value or n2 is smaller than n1
                nums1.insert(i, n2)  # this is O(n)
                nums1.pop()
                # all items in nums1 shifted right
                p1 += 1
                p2 += 1

    def merge_optimized(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        2022-07-15 08:52:55
        Runtime: 45 ms (79%)
        Memory Usage: 13.9 MB (38%)

        Some optimizations
        """
        if n == 0:
            return
        # if nums2 starts with a number gte to the last number in nums1, merge and return
        if nums1[m - 1] <= nums2[0]:
            nums1[m:] = nums2
            return
        p2 = p1 = 0
        for i in range(m + n):
            n1, n2 = nums1[p1], nums2[p2]
            # if we're done with numbers in nums1, merge the rest from nums2 and return
            if p1 >= m + p2:
                nums1[p1:] = nums2[p2:]
                return
            # if n1 is lte n2, advance pointer in nums1
            if n1 <= n2:
                p1 += 1
            else:
                # n2 is smaller than n1. insert in place
                nums1[i:] = [n2] + nums1[i : m + n - 1]
                p1, p2 = p1 + 1, p2 + 1  # move pointers in both arrays
                # nums2 exhausted. we're done!
                if p2 == n:
                    break

    def merge_with_slice(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        2022-09-20 08:39:48
        Runtime: 40 ms (92%)
        Memory Usage: 14 MB (38%)

        2 pointers seem to work better with WHILE loop
        because it's easier to move them conditionally

        Do not return anything, modify nums1 in-place instead.
        m = true length of the nums1
        n = true length of the nums2
        m + n == len(nums1)
        0 represents null
        [1] m=1 [] n=0 -> [1]
        [0] m=0 [1] n=1 -> [1]
        [1, 3, 0] m=2 [2] n=1 -> [1, 2, 3]
        """
        if not nums2:
            return
        if m == 0:
            nums1[:] = nums2
            return
        i = j = 0
        while i < m + n and j < n:
            if nums1[i] > nums2[j]:
                # num1[i: m+n-1] gets smaller each time
                nums1[i:] = nums2[j : j + 1] + nums1[i : m + n - 1]
                j += 1
            i += 1
        if j < n:
            nums1[m + j :] = nums2[j:]

    def merge_with_slice_better(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        2022-11-01 08:42:37

        Exits the loop when:
        a. p1 advances past the last non-padding element
            - when p1 == m + p2(number of elements copied over from nums2)
        b. p2 reaches the end of nums2 array
            - all elements in p2 are spliced into nums1

        We need to append the rest of num2 in case of a.
        In case of b, this would be no-op (appending None)

        This has less line, but more complex than going backward to copy over bigger number from the two arrays.
        REMEMBER:
        - Going backward for inline operation allows us to keep the original data
        """
        p1 = p2 = 0
        while p2 < n and p1 < m + p2:
            if nums1[p1] > nums2[p2]:
                nums1[:] = nums1[:p1] + [nums2[p2]] + nums1[p1 : m + n - 1]
                p2 += 1
            p1 += 1
        nums1[m + p2 :] = nums2[p2:]

    def merge_sort_desc(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        2022-07-16 21:36:43
        Runtime: 51 ms (65%)
        Memory Usage: 13.8 MB (86%)

        - two arrays are already sorted
        - larger of the last items from both array will be inserted into the last slot of first array
        - If we run out of 2nd array first, we know that the 1st array is already sorted
        - If we run out of 1st array before 2nd, we need to loop through the remaining 2nd array to fill out the 1st array

        - Working from the end of the array is better since we can keep the original items while writing values.
        - Can we do this from the beginning of the array?
          -> No. Unless we all items in nums1 is less than the first item in nums2,
          some of the values in nums1 will be overwritten by values from nums2 and
          we need to store those values somewhere so that we can copy them over after the last value copied from nums2
          -> working backward solves this problem

        TIL: If there's a way to not override the original data, go for it!
        """
        p1, p2, i = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
        while p2 >= 0:
            nums1[i] = nums2[p2]
            p2 -= 1
            i -= 1

    def merge_desc_slice(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        2022-11-02 07:50:32

        slice instead of looping to copy over remainders from nums2
        """
        i = m + n - 1
        p1 = m - 1
        p2 = n - 1
        # p1 == -1 : we compared all numbers in nums1, but there might be some numbers left in nums2
        # p2 == -1 : we compared all numbers in nums2, nums1 is already sorted
        while p1 > -1 and p2 > -1:
            if nums1[p1] < nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1
            i -= 1
        # insert the slice if there are remaining numbers in nums2
        if p2 >= 0:
            nums1[: i + 1] = nums2[: p2 + 1]

    def merge_desc_optimized(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        2022-09-21 08:22:39
        Runtime: 43 ms (87%)
        Memory Usage: 14 MB (38%)

        Use for loop to iterate backward on first array.
        if pointers go out of range on either array,
        we concat the remaining (reached the end of num1) OR
        return None (reached the end of nums2 - nums1 is already sorted)

        This is easier to understand since all conditions are in one place.
        """
        # set pointers at the last elements
        p1, p2 = m - 1, n - 1
        # iterate backward on first array
        for p1 in range(len(nums1) - 1, -1, -1):
            if p1 < 0:
                nums1[: p1 + 1] = nums2[: p2 + 1]
                return None
            if p2 < 0:
                return None
            if nums1[p1] > nums2[p2]:
                nums1[p1] = nums1[p1]
                p1 -= 1
            else:
                nums1[p1] = nums2[p2]
                p2 -= 1

    def merge_backward(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        2022-12-06 19:41:35
        creates one pointer for insert position starting from the end of array
        and repurposes argument as pointers to compare values.

        Easiest to understand
        """
        i = m + n - 1
        m, n = m - 1, n - 1
        while m >= 0 and n >= 0:
            if nums1[m] < nums2[n]:
                nums1[i] = nums2[n]
                n -= 1
            else:
                nums1[i] = nums1[m]
                m -= 1
            i -= 1
        if m < 0:
            nums1[: n + 1] = nums2[: n + 1]

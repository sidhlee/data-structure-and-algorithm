"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

from collections import Counter
from typing import List


class Solution:
    def intersect_counter(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        2022-06-15T12:56:03.460Z
        Runtime: 46 ms
        Memory Usage: 13.9 MB

        Constraints allow us to create hashmap ( <= 1000) to avoid O(n^2) loops
        Use collections.Counter and binary operator (&) to get the intersection of to counters

        Counter & Counter -> intersection
        Counter | Counter -> Union
        c1 - c2 -> left outer
        c.most_common() -> sorts counter by frequency
        """
        return (Counter(nums1) & Counter(nums2)).elements()

    def intersect_forgot_counter_operations(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        """
        2022-06-24T12:00:54.981Z
        Runtime: 58 ms (78%)
        Memory Usage: 14 MB (51%)

        Basically same as above, but longer.
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        result = []
        for n in c1:
            if c2[n]:
                result += [n] * min(c1[n], c2[n])
        return result

    def intersect_only_one_counter(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        """
        2024-02-09 05:27:31
        Runtime: 51ms (56%)
        Memory Usage: 16.8 MB (58%)

        only use one counter -> less memory usage + faster
        Length is capped at 1000, so it's not a big deal to use a counter
        and which list to use as the counter doesn't matter
        """
        c = Counter(nums2)
        result = []
        for num in nums1:
            if num in c and c[num] > 0:
                result.append(num)
                c[num] -= 1
        return result

"""
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0

Constraints:

0 <= n <= 5 * 106

103 % 10 == 3
t == 10
lsd == 0

"""


class Solution:
    def countPrimes_mark_off(self, n: int) -> int:
        """
        2022-07-24 12:26:17
        Runtime: 4051 ms (71%)
        Memory Usage: 55.5 MB (55%)

        Use n space to mark off to reduce the number of nested loop

        Slow approach:

        def is_prime(self, n):
            # many conditions to reduce the amount of iteration
            # If passes through all the conditions, loop through a list (eg. prime numbers)

        This is slow because for every single number below n, we're plugging that number through the checker.

        Marking off strategy is faster because with each iteration the remaining numbers to go through gets reduced greatly.
        --> Use space to incrementally reduce the workload!
        """
        if n <= 2:
            return 0
        nums = [1] * n
        nums[0] = nums[1] = 0
        for i in range(2, n):
            if nums[i]:
                for j in range(i * i, n, i):
                    nums[j] = 0
        return len([x for x in nums if x])

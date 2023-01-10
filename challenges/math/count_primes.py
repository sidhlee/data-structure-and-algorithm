import math

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

    def countPrimes_again(self, n: int) -> int:
        """
        2022-09-27 20:02:42
        """
        nums = [0, 0] + [1] * (n - 2)
        for i in range(2, len(nums)):
            if nums[i]:
                # start from i * i since i * 2, i * 3, .. i * (i - 1) are already marked as false
                # in previous iterations
                for j in range(i * i, n, i):
                    nums[j] = 0
        return sum(nums)

    def countPrimes_set_fails_time_limit(self, n: int) -> int:
        """
        2022-11-15 08:12:53
        Uses the same logic as above, but maybe set.discard(val) is slower than setting list value at a given index.
        - discard needs to check whether the value exists in the set -> 2x more things to do for each iteration.

        If you don't need to iterate, and need to toggle switches on integer value, list is faster than set.
        """
        # don't need this since sieve would be empty when n <= 2
        # if n <= 2:
        #     return 0
        sieve = {n for n in range(2, n)}
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if i in sieve:
                for j in range(i * i, n, i):
                    sieve.discard(j)
        return len(sieve)
    
    def countPrimes_sieve_upto_sqrt(self, n: int) -> int:
        '''
        2022-12-17 16:43:13
        '''
        if n <= 2:
            return 0
        sieve = [0, 0] + [1] * (n - 2)
        # Because the inner loop is starting from i^2, we don't even need to start the outer loop if i * i >= n. 
        # so we're looping while i * i < n -> i < sqrt(n)
        for i in range(2, math.floor(n ** 0.5) + 1):
            if sieve[i]:
                # i * 2, i * 3, ... i * (i - 1) are already marked off in previous iterations
                for j in range(i * i, n, i):
                    sieve[j] = 0
        return sum(sieve)
    
    def countPrimes_best(self, n: int) -> int:
        '''
        2023-01-10 08:36:26
        '''
        sieve = [0, 0] + [1] * (n - 2) # index up to n - 1
        for i in range(2, math.floor(math.sqrt(n)) + 1): # when n = 10, increments up to 3
            for j in range(i * i, n, i):
                sieve[j] = 0
        return sum(sieve)

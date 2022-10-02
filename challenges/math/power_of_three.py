"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true

Constraints:

-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?

9 27 81 243 729 2187 6561 19683
"""


class Solution:
    def isPowerOfThree_brute_force(self, n: int) -> bool:
        """
        2022-07-25 07:47:01
        Runtime: 200 ms (15%)
        Memory Usage: 13.9 MB (57%)

        Should've spent more time straightening out:
        - the min condition to get into loop
        - expected outcome at the end of the loop
        """
        if n == 0:
            return False
        while abs(n) > 1:
            if n == -3 or n % 3 != 0:
                return False
            n /= 3
        return True

    def isPowerOfThree_loop_and_match(self, n: int) -> bool:
        """
        2022-07-25 08:00:36
        Runtime: 116 ms (66%)
        Memory Usage: 13.8 MB (57%)

        * If the output is boolean, comparing in return statement can be an option.
        * Find the highest filter before getting into the loop
            -> if it's not divisible by 3, don't even get into it
            -> power of 3 (not -3) is always > 0 (1 for 0 power)
        * Think about the expected outcome at the end of the loop
            -> n becomes 1
        * Check the expected final outcome. All input that didn't get into the loop will not match.

        """
        while n % 3 == 0 and n > 0:
            n /= 3
        return n == 1

    def isPowerOfThree_use_constraints(self, n: int) -> bool:
        """
        2022-07-25 08:19:30
        Runtime: 130 ms (52%)
        Memory Usage: 13.8 MB (96%)

        given constraints: -2^31 <= n <= 2^31 - 1
        -> 1 <= n <= 2147483647 to be the power of 3
        The biggest power of 3 within the constraint: 3486784401 = 3 * 3 * 3 * ... * 3
        -> power of three must be only composed with 3's
        """
        return n > 0 and 3**19 % n == 0

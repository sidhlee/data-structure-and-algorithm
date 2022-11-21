"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        """
        2022-06-25T22:52:39.033Z
        Runtime: 19 ms (99.96%)
        Memory Usage: 14 MB (0%)

        If the system indeed does not allow int64, we could use try and except to return 0
        """
        is_negative = x < 0
        x = list(str(x).lstrip("-"))
        x.reverse()
        x = "".join(x)

        if (is_negative and -int(x) < -(2**31)) or (
            not is_negative and int(x) > 2**31 - 1
        ):
            return 0

        return int(x) if not is_negative else -1 * int(x)

    def reverse_string_with_negative_step(self, x: int) -> int:
        """
        2022-06-25T23:00:31.655Z
        Runtime: 41 ms (74%)
        Memory Usage: 13.9 MB (63%)

        In python, you can reverse string with negative step slicing.
        """
        r = int(str(abs(x))[::-1])
        if (r > pow(2, 31) - 1) or (r < pow(-2, 31)):
            return 0
        return int(r) if x >= 0 else -int(r)

    def reverse_keep_the_sign(self, x: int) -> int:
        """
        2022-08-20 20:54:05
        Runtime: 30 ms (97%)
        Memory Usage: 14 MB (0%)

        stripping sign on the reversed number seems better.
        can use this if we somehow need to keep that information within the reversed string.
        (but hey, reversed and the original integer should ALWAYS have the same sign!)
        """
        r = "".join(list(reversed(str(x))))
        r = int(r) if r[-1] != "-" else -int(r[:-1])
        return r if -(2**31) <= r <= 2**31 - 1 else 0

    def reverse_math(self, x: int) -> int:
        """
        2022-10-16 17:09:45
        Runtime: 36 ms (91%)
        Memory Usage: 13.8 MB (97%)

        mod 10 to get LSD. multiple previous result by 10 and add the LSD
        """
        res = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x > 0:
            lsd = x % 10
            if res * 10 + lsd < 2**31:
                res = res * 10 + lsd
            # or catch out of range error
            else:
                return 0
            x = x // 10
        return sign * res

    def reverse_math2(self, x: int) -> int:
        """
        2022-11-20 19:13:40
        sign the LSD before adding to the result
        """
        res = 0
        sign = 1 if x >= 0 else -1
        x = x * sign
        while x:
            lsd = x % 10
            res = res * 10 + sign * lsd
            if res > 2**31 - 1 or res < -(2**31):
                return 0
            x //= 10
        return res

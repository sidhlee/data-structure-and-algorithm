"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1

Constraints:

0 <= x, y <= 231 - 1
"""


class Solution:
    def hammingDistance_bitwise_1(self, x: int, y: int) -> int:
        """
        2022-07-28 08:30:04
        Runtime: 46 ms (52%)
        Memory Usage: 13.9 MB (61%)

        First attempt with bitwise operation.
        1. Get xor between x and y. different digit becomes 1 and matching digit becomes 0.
        2. While right-shifting xor, increment distance if xor's LSD is 1 (does not match)
        """
        count = 0
        xor = x ^ y
        while xor:
            if xor & 1 == 1:
                count += 1
            xor >>= 1
        return count
    
    def hammingDistance_add_lsd(self, x: int, y: int) -> int:
        '''
        2022-12-18 19:30:59
        '''
        z = x ^ y
        distance = 0
        while z:
            distance += (z & 1)
            z >>= 1
        return distance

    def hammingDistance_one_line(self, x: int, y: int) -> int:
        """
        2022-07-28 08:38:22
        Runtime: 36 ms (82%)
        Memory Usage: 14 MB (0%)

        Uses O(n) space for creating binary string
        """
        return bin(x ^ y).count("1")

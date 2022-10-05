from collections import Counter

"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:

The input must be a binary string of length 32.

Follow up: If this function is called many times, how would you optimize it?
"""


class Solution:
    def hammingWeight_transforms(self, n: int) -> int:
        """
        2022-07-27 07:18:31
        Runtime: 41 ms (70%)
        Memory Usage: 13.9 MB (50%)

        - bin(int) returns binary string with "0b" prefix. fastest.
        """
        return len([x for x in str(bin(n)) if x == "1"])

    def hammingWeight(self, n: int) -> int:
        '''
        2022-10-02 13:40:27
        Runtime: 40 ms (79%)
        Memory Usage: 13.8 MB (50%)

        - format(n, 'b') returns binary string without prefix, but little slower than bin()
        '''
        return Counter(format(n, "b"))["1"]

    def hammingWeight_bitwise(self, n: int) -> int:
        """
        2022-07-27 08:25:49
        Runtime: 44 ms (62%)
        Memory Usage: 13.9 MB (50%)

        bitwise operator & returns 1 if the LSB matches 1 else 0.
        >> (right shift) shifts bits to the right the given number of times.

        eg.
        n = 11 -> 1011(2)
        1011 & 1 -> 1
        1011 >> 1 -> 101
        101 & 1 -> 1
        101 >> 1 -> 10
        10 & 1 -> 0
        10 >> 1 -> 1
        1 & 1 -> 1
        1 >> 1 -> 0
        """
        weight = 0
        while n:
            weight += n & 1
            n >>= 1
        return weight

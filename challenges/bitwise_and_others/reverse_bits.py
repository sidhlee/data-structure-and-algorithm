"""
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. 
In this case, both input and output will be given as a signed integer type. 
They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. 
Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

Constraints:

The input must be a binary string of length 32

Follow up: If this function is called many times, how would you optimize it?
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        2022-07-29 08:31:41
        Runtime: 37 ms (86%)
        Memory Usage: 13.9 MB (50%)

        Do the for loop since the length of the binary string is fixed at 32.
        - concat '1' to the result string if the lsd is 1, otherwise concat '0'
        - right shift input to go to the next least-significant-digit
        - convert the bin string into integer after the loop
        """
        bin_str = ""
        for i in range(32):
            bin_str += "1" if n & 1 else "0"
            n >>= 1
        return int(bin_str, 2)

    def reverseBits_no_conversion(self, n: int) -> int:
        """
        From 22ms submission

        Use index to select the bit from the right and
        shift it to the left to keep merging it with the result at the correct places.
        """
        res = 0
        for i in range(32):
            # select ith bit from the right
            bit = (n >> i) & 1
            # shift the selected bit to the ith from the left and
            # use OR to merge it with the current result
            res = res | bit << (31 - i)

        return res
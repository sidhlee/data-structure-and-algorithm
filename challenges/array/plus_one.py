"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""

from typing import List


class Solution:
    def plusOne_convert_to_int(self, digits: List[int]) -> List[int]:
        """
        2022-06-16T11:13:36.645Z
        Runtime: 37 ms (80.25%)
        Memory Usage: 13.8 MB (96.46%)
        """
        s = "".join(map(str, digits))
        n = int(s)
        s = str(n + 1)
        return [n for n in s]

    def plusOne_loop_once_and_less_lines(self, digits: List[int]) -> List[int]:
        """
        2022-06-16T11:20:50.346Z
        Runtime: 33 ms (91.09%)
        Memory Usage: 13.8 MB (96.46%)

        join & map (2n) -> for (1n)
        """
        s = ""
        for d in digits:
            s += str(d)
        s = str(int(s) + 1)
        return [n for n in s]

    def plusOne_one_line(self, digits: List[int]) -> List[int]:
        """
        Runtime: 48 ms (46.37%)
        Memory Usage: 13.8 MB (96.46%)

        This was 21ms solution but leetcode stats are not consistent.

        Use tuple instead of list whenever you can:
        - Tuples tend to perform better than lists in almost every category
        - https://stackoverflow.com/a/22140115
        """
        return list(str(int("".join((str(d) for d in digits))) + 1))

    def plusOne_tuple_over_list(self, digits: List[int]) -> List[int]:
        """
        2022-06-24T12:36:43.689Z
        Runtime: 36 ms (86%)
        Memory Usage: 13.7 MB (96%)

        Use tuple when you're not mutating it
        - Tuples only use minimum memory it requires
        - Tuples have little bit faster lookup/instantiation time.
          - This adds up on large iterations
        """
        plus_one = int("".join((str(n) for n in digits))) + 1
        return list(str(plus_one))

    def plusOne_math(self, digits: List[int]) -> List[int]:
        """
        2022-06-16T11:46:23.787Z
        Runtime: 56 ms
        Memory Usage: 13.8 MB
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    return digits
            else:
                digits[i] += 1
                return digits
        return digits

    def plusOne_math_better(self, digits: List[int]) -> List[int]:
        """
        2022-06-16T12:11:15.460Z
        Runtime: 54 ms (31.12%)
        Memory Usage: 13.9 MB (57.34%)

        Moved the check i == 0 out of the loop because once out of the loop,
        it is given that i == 0.
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

    def plusOne_math_fewer_lines(self, digits: List[int]) -> List[int]:
        """
        2022-08-16 08:49:41
        Runtime: 31 ms (97%)
        Memory Usage: 13.7 MB (97%)

        Since only thing we do inside condition block is assignment,
        condensed if else block into 1 line.
        """
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + 1 if digits[i] != 9 else 0
            if digits[i] != 0:
                return digits
        return [1] + digits

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Hint #1  
Problem is simpler to solve by working the string from back to front and using a map.
"""


class Solution:
    def romanToInt_right_to_left(self, s: str) -> int:
        """
        2022-07-26 07:42:27
        Runtime: 56 ms (83%)
        Memory Usage: 13.8 MB (76%)

        Iterate backward following hint
        """
        TO_NUM = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        chars = list(s)
        num = TO_NUM[chars[-1]]
        for i in range(len(chars) - 2, -1, -1):
            if chars[i] == "I" and chars[i + 1] in ("V", "X"):
                num -= 1
                continue
            if chars[i] == "X" and chars[i + 1] in ("L", "C"):
                num -= 10
                continue
            if chars[i] == "C" and chars[i + 1] in ("D", "M"):
                num -= 100
                continue
            num += TO_NUM[chars[i]]
        return num

    def romanToInt_left_to_right(self, s: str) -> int:
        """
        2022-07-26 07:53:05
        Runtime: 55 ms (85%)
        Memory Usage: 13.9 MB (76%)

        Left to right seems to work fine and looks less complicated.
        Also don't need to convert to a list
        """
        TO_NUM = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = TO_NUM[s[-1]]
        for i in range(len(s) - 1):
            if s[i] == "I" and s[i + 1] in ("V", "X"):
                num -= 1
                continue
            if s[i] == "X" and s[i + 1] in ("L", "C"):
                num -= 10
                continue
            if s[i] == "C" and s[i + 1] in ("D", "M"):
                num -= 100
                continue
            num += TO_NUM[s[i]]
        return num

    def romanToInt_backward_2(self, s: str) -> int:
        """
        2022-10-02 02:10:46
        we don't need to convert string to list.
        Also, if..continue can just be if elif
        """
        rom_to_num = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = rom_to_num[s[len(s) - 1]]
        for i in range(len(s) - 2, -1, -1):
            if s[i] == "I" and s[i + 1] in ("X", "V"):
                result -= 1
            elif s[i] == "X" and s[i + 1] in ("C", "L"):
                result -= 10
            elif s[i] == "C" and s[i + 1] in ("M", "D"):
                result -= 100
            else:
                result += rom_to_num[s[i]]
        return result

    def romanToInt_backward3(self, s: str) -> int:
        """
        2022-11-17 08:30:11
        collapses 3 checks into one condition

        Long OR condition can be further simplified with if dict[char] < dict[right_char]
        """
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        right_char = None
        for char in s[::-1]:
            if (
                (char == "I" and right_char in ("V", "X"))
                or (char == "X" and right_char in ("L", "C"))
                or (char == "C" and right_char in ("D", "M"))
            ):
                res -= dict[char]
            else:
                res += dict[char]
            right_char = char
        return res

    def romanToInt_collapsing_elifs(self, s: str) -> int:
        """
        2022-10-02 02:25:17
        If you can find the common logic across multiple elif statements,
        you can collapse them into one condition!
        """
        rom_to_num = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = rom_to_num[s[len(s) - 1]]
        for i in range(len(s) - 2, -1, -1):
            if rom_to_num[s[i]] < rom_to_num[s[i + 1]]:
                result -= rom_to_num[s[i]]
            else:
                result += rom_to_num[s[i]]
        return result

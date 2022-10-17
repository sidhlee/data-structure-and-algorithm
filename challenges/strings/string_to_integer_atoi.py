import re

"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. This determines if the final result is negative or positive respectively.
Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached.
The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
then clamp the integer so that it remains in the range. 
Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""


class Solution:
    """
    2022-06-26T21:54:41.866Z
    Runtime: 32 ms (97%)
    Memory Usage: 13.8 MB (79%)

    We can probably make this simpler by taking advantage of s.length <= 200

    Could use this at the end:
    min(max(num, -pow(2, 31)), pow(2, 31) - 1)
    """

    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == "":
            return 0

        sign = s[0] if s[0] in ("+", "-") else None
        num = ""
        for i in range(1 if sign else 0, len(s)):
            if not s[i].isnumeric():
                break
            num += s[i]

        if num == "":
            return 0

        num = -1 * int(num) if sign == "-" else int(num)

        return min(max(num, -pow(2, 31)), pow(2, 31) - 1)

    def myAtoi_shorter(self, s: str) -> int:
        '''
        2022-08-23 18:54:58
        Runtime: 40 ms (87%)
        Memory Usage: 13.9 MB (29%)

        shorter because empty string is checked later
        '''
        s = s.strip()
        sign = 1
        if s and s[0] in ("-", "+"):
            sign = 1 if s[0] == '+' else -1
            s = s[1:]
        for i, char in enumerate(s):
            if not char.isnumeric():
                s = s[:i]
                break
        if not s:
            return 0
        return min(2**31 - 1, max(-(2**31), int(s) * sign))
    
    def myAtoi_build_res_with_math(self, s: str) -> int:
        '''
        2022-10-17 07:28:46
        Runtime: 57 ms (66%)
        Memory Usage: 13.9 MB (78%)
        
        Instead of converting ranges of string into int, build the result inside the loop
        one digit at a time.
        This is not necessary for the current requirement.
        '''
        s = s.strip()
        sign = 1
        res = 0
        if s and s[0] in ['-', '+']:
            sign = int(s[0] + '1')
            s = s[1:]
        for char in s:
            if not char.isnumeric():
                break
            res = res * 10 + int(char)
        return min(max(sign * res, -2**31), 2**31 - 1)

    def myAtoi_regex(self, s: str) -> int:
        '''
        2022-08-23 19:30:58
        Runtime: 58 ms (45%)
        Memory Usage: 13.9 MB (80%)
        '''
        match = re.search(r'^\s*([-+]?\d+)', s)
        num_str = match.group(1) if match else None
        return min(2**31 - 1, max(-(2**31), int(num_str))) if num_str else 0

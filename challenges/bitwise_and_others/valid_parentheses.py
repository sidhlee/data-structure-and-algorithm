"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Hint #1
An interesting property about a valid parenthesis expression is that a sub-expression of a valid expression should also be a valid expression.
(Not every sub-expression) e.g.
{ { } [ ] [ [ [ ] ] ] } is VALID expression
          [ [ [ ] ] ]    is VALID sub-expression
  { } [ ]                is VALID sub-expression
Can we exploit this recursive structure somehow?

Hint #2  
What if whenever we encounter a matching pair of parenthesis in the expression, we simply remove it from the expression? 
This would keep on shortening the expression. e.g.
{ { ( { } ) } }
      |_|

{ { (      ) } }
    |______|

{ {          } }
  |__________|

{                }
|________________|

VALID EXPRESSION!

Hint #3
The stack data structure can come in handy here in representing this recursive structure of the problem. 
We can't really process this from the inside out because we don't have an idea about the overall structure.
But, the stack can help us process this recursively i.e. from outside to inwards.
"""


class Solution:
    def isValid_check_and_return(self, s: str) -> bool:
        """
        2022-08-04 05:54:08
        Runtime: 57 ms (29%)
        Memory Usage: 13.8 MB (98%)
        """
        stack = []
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            else:
                try:
                    last_open_bracket = stack.pop()
                    if c == ")" and last_open_bracket != "(":
                        return False
                    if c == "]" and last_open_bracket != "[":
                        return False
                    if c == "}" and last_open_bracket != "{":
                        return False
                except IndexError:
                    return False
        return len(stack) == 0

    def isValid_check_before_pop(self, s: str) -> bool:
        """
        2022-08-04 06:15:10
        Runtime: 34 ms (90%)
        Memory Usage: 13.8 MB (71%)

        - If you're catching IndexError, replace it with additional check before pop
        - If you're matching a pair of something with many if statements, replace them with a map
        """
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            else:
                if not stack or stack.pop() != close_to_open[c]:
                    return False
        return len(stack) == 0

    def isValid_check_for_quick_return(self, s: str) -> bool:
        """
        2022-11-19 17:28:19
        If a certain condition allows you to return early, check that condition first.
        eg. If the current value is closing bracket, but if the stack is empty or the value on top of the stack is not the matching open bracket -> invalid
        """
        dict = {")": "(", "]": "[", "}": "{"}
        stack = []
        for bracket in s:
            if bracket in dict:
                if not stack or stack.pop() != dict[bracket]:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0

    def isValid_pop_only_if_match(self, s: str) -> bool:
        """
        2022-12-20 05:35:14
        popping during the match seems to be better since
        we don't need to keep the opening bracket when the current character is closing one.
        No match -> return False
        match -> continue
        """
        o2c = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in o2c:
                if not stack or stack[-1] != o2c[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack

    def isValid_loop_from_second(self, s: str) -> bool:
        """
        2023-01-13 07:24:30
        Take advantage of the assumption and start looping from second item
        """
        closings = {")": "(", "]": "[", "}": "{"}
        stack = [s[0]]
        for c in s[1:]:
            if c in closings:
                if not stack or stack[-1] != closings[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0

    def isValid_easier_to_read(self, s: str) -> bool:
        """
        2023-06-19 06:55:05
        """
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in close_to_open:
                # if it's a closing bracket, stack shouldn't be empty and the last bracket in stack should be the matching open bracket
                if not stack or stack.pop() != close_to_open[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

    def isValid_simple(self, s: str) -> bool:
        """
        2024-04-02 06:34:48
        This is just validating, so we can use the popped result immediately and lose it.
        """
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}
        for bracket in s:
            if bracket in close_to_open:
                if not stack or stack.pop() != close_to_open[bracket]:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0

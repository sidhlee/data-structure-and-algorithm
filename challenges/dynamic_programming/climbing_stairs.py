"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2

Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3

Explanation: There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45

Hint1:
To reach nth step, what could have been your previous steps? (Think about the step sizes)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Runtime: 32 ms (90%)
        Memory Usage: 13.8 MB (96%)

        At every decision point we can either step or skip -> "binary decision tree"
        - Each non-null leaf counts as 1 and we stop either at 1 or 0
        - At every node, the # of possibilities is the sum of possibilities from left and right child.
        - There are duplicates of the same sub-trees -> use memoization.

        './climbing_stairs_1.png'

        TODO: iterative solution. - calculate parent node's possibilities by summing up left and right.
        """
        dict = {}

        def inner(distance):
            # when distance becomes 1, we can stop since there is only one way to resolve from here.
            if 0 <= distance <= 1:
                return 1
            # not needed since we stop at distance == 1
            # if distance < 0:
            #     return 0
            left = dict.get(distance - 1) or inner(distance - 1)
            right = dict.get(distance - 2) or inner(distance - 2)
            result = left + right
            dict[distance] = result
            return result

        return inner(n)

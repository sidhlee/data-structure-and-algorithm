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

    def climbStairs_bottom_up(self, n: int) -> int:
        '''
        2022-09-23 08:57:21
        Runtime: 28 ms (97%)
        Memory Usage: 13.8 MB (96%)

        decision tree until stairs_traveled = n
                       0  1, 2, 3, 4, 5
        possible ways: 8  5  3  2  1  
        perm from any one spot -> 1 or 2 steps
        BOTTOM UP appraoch:
        - From step 4, we have 1 way to reach step 5
        - From step 3, we have 2 ways (3 > 4 > 5, 3 > 5)  
        - From step 2, we can get to step 4(1) or step 3(2): 1 + 2 = 3
        - From step 1, we can get to step 3(2) or step 2(3): 2 + 3 = 5
        - From step 0, we can get to step 2(3) or step 1(5): 3 + 5 = 8
        perms at current step depends on the the perms at step + 1 and perms at step + 2

        Time: we start computing bottom up from step 2 to step 0 -> O(n - 2) 
        space: we need 2 temp vars to store perms on 2 steps we can land on from the current step -> O(2)
        '''
        ways_one_left = 0
        ways_two_left = 1
        for i in range(n - 1, -1, -1):
            ways_two_left, ways_one_left = ways_two_left + ways_one_left, ways_two_left
        return ways_two_left
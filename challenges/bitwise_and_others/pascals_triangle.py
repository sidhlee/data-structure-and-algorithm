from typing import List

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
  1 5 10 10 5 1
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:

1 <= numRows <= 30
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        2022-08-02 08:31:30
        Runtime: 43 ms (64%)
        Memory Usage: 13.9 MB (66%)

        O(n^2) solution. could optimize by taking advantage of the array's symmetry.
        but the difference wouldn't be much because the numRow has the upper bound of 30.

        writing out the example with indexes helps us understand the pattern
        j 0    1      2
        n 1    2      3        4          5                 6
        [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1], [1, 5, 10, 10, 5, 1]]
        """

        res = [[1]]
        for i in range(1, numRows):
            sub_arr = [1]
            for j in range(1, i):
                sub_arr.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(sub_arr + [1])
        return res

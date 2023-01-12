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
    def generate_look_behind(self, numRows: int) -> List[List[int]]:
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
        # Use the constraint to start with the first row
        res = [[1]]
        # now you can start from the second row
        for i in range(1, numRows):
            sub_arr = [1]
            # also start from the second index so that we can look behind
            for j in range(1, i):
                # not getting here when i = 1
                # starts from 3rd row & working with prev row so we end at the same index as prev row
                sub_arr.append(res[i - 1][j - 1] + res[i - 1][j])
            # after loop, just need to add 1 to the curr arr    
            res.append(sub_arr + [1])
        return res

    def generate_look_ahead(self, numRows: int) -> List[List[int]]:
        '''
        2022-10-07 08:53:21
        Runtime: 32 ms (94%)
        Memory Usage: 13.8 MB (66%)

        look-behind works better since you don't need condition to check index range
        starting late and looking behind is much simpler in terms of managing index range
        '''
        rows = []
        for i in range(numRows):
            curr_row = [1]
            for j in range(i):
                prev_row = rows[i - 1]
                # append 0 as the last number
                curr_row.append(prev_row[j] + (prev_row[j + 1] if j < len(prev_row) - 1 else 0))
            rows.append(curr_row)
        return rows

    def generate_use_symmetry(self, numRows: int) -> List[List[int]]:
        '''
        2023-01-12 08:13:57
        calculate only upto the middle and get the rest by reversing.
        made it easier to read by using variables
        '''
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        for row_idx in range(2, numRows):
            curr_row = [1]
            prev_row = res[row_idx - 1]
            # row_idx == last_index_within_a_row
            for i in range(1, row_idx // 2 + 1):
                curr_row.append(prev_row[i-1] + prev_row[i])
            i_in_middle = row_idx / 2 == i
            start_from = i - 1 if i_in_middle else i
            curr_row += curr_row[start_from::-1]
            res.append(curr_row)                
        return res
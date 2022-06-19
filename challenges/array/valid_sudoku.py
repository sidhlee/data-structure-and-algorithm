"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1: 
'./valid_sudoku_example1.png'

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

"""
from typing import List


class Solution:
    def isValidSudoku_floor_division(self, board: List[List[str]]) -> bool:
        """
        2022-06-19T22:11:55.519Z
        Runtime: 99 ms
        emory Usage: 13.9 MB

        In order to figure out how to use i and j to create the lists of subgrids,
        it was helpful to write out examples like this to see and get the intuition.

        [00 01 02 10 11 12 20 21 22]
        [03 04 05 13 14 15 23 24 25]
        [06 07 08 16 17 18 26 27 28]
        [30 31 32 40 41 42 50 51 52]
        [33 34 35 43 44 45 53 54 55]
        [36 37 38 46 47 48 56 57 58]

        We can use nested loop since we have small upper bound.
        ...


        """
        rows = [[], [], [], [], [], [], [], [], []]
        cols = [[], [], [], [], [], [], [], [], []]
        subgrids = [[], [], [], [], [], [], [], [], []]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].append(board[i][j])
                if board[j][i] != ".":
                    cols[i].append(board[j][i])
                m = 3 * (i // 3) + j // 3
                n = (i % 3) * 3 + j % 3
                # tune the locators here
                # print(m, n)
                if board[m][n] != ".":
                    subgrids[i].append(board[m][n])
        for nums in rows + cols + subgrids:
            if len(nums) != len(set(nums)):
                return False
        return True

    def isValidSudoku_return_early(self, board: List[List[str]]) -> bool:
        """
        2022-06-19T22:41:12.019Z
        Runtime: 91 ms
        Memory Usage: 13.9 MB

        You don't need to wait till the all lists are completed.
        - Use set to find existing number with O(1).
        - Validate within the inner loop to return as early as possible
        - Clear set after inner loop is done to limit memory usage
        """
        group = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] in group:
                    return False
                if board[i][j] != ".":
                    group.add(board[i][j])
            group.clear()
        for i in range(9):
            for j in range(9):
                if board[j][i] in group:
                    return False
                if board[j][i] != ".":
                    group.add(board[j][i])
            group.clear()
        for i in range(9):
            for j in range(9):
                m = 3 * (i // 3) + j // 3
                n = (i % 3) * 3 + j % 3
                if board[m][n] in group:
                    return False
                if board[m][n] != ".":
                    group.add(board[m][n])
            group.clear()
        return True

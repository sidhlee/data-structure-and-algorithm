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
'./valid_sudoku_1.png'

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
    def isValidSudoku_create_lists_first(self, board: List[List[str]]) -> bool:
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

        2022-08-18 08:59:46
        But this solution creates all lists to loop upfront even though we could return early.
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

        2022-08-18 09:02:07
        This solutions makes the assumption that all cells have either "." or values between [1, 9]
        , which is NOT provided by the requirements.
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

    def isValidSudoku_with_slicing(self, board: List[List[str]]) -> bool:
        """
        2022-06-25T20:43:00.141Z
        Runtime: 91 ms (98%)
        Memory Usage: 13.8 MB (99%)

        Couldn't remember adding to a set to check duplicates inside the loop
        -> this should be faster because we're returning false as soon as possible
        without filtering through the whole array. (wouldn't make much difference because len(arr) is always 9)
        -> this also allows to loop through the subgrid and validate value by value.

        Interestingly this approach is up to par with the above solution,
        probably because the size of the list is constant at 81.

        Notes to visualize the problem:
            - indices to find ways to form subgrid
            123 00 01 02  03 04 05
            456 10 11 12  13 14 15
            789 20 21 22  23 24 25

            - copied from test input to verify subgrid slicing
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]

        """

        def is_valid(numbers):
            # also makes the same assumption as above
            arr = [x for x in numbers if x != "."]
            return len(arr) == len(set(arr))

        for row in board:
            if not is_valid(row):
                return False
        for col in list(map(list, zip(*board))):
            if not is_valid(col):
                return False
        for i in range(3):
            for j in range(3):
                s = slice(3 * j, 3 * (j + 1))
                subgrid = board[3 * i][s] + board[3 * i + 1][s] + board[3 * i + 2][s]
                if not is_valid(subgrid):
                    return False

        return True

    def isValidSudoku_robust_validator(self, board: List[List[str]]) -> bool:
        """
        2022-08-19 08:06:59
        Runtime: 99 ms (94%)
        Memory Usage: 13.9 MB (83%)

        - Uses util functions outside the class -> might be faster since reusing functions between testcases
        - is_valid function is more robust
        """
        for row in board:
            if not is_valid(row):
                return False
        # we don't need reversed since we don't care about the order when validating
        for col in list(zip(*reversed(board))):
            if not is_valid(col):
                return False
        for i in range(3):
            for j in range(3):
                if not is_valid(get_subgrid(board, i, j)):
                    return False
        return True
    
    def isValidSudoku_readable(self, board: List[List[str]]) -> bool:
        '''
        2022-12-23 07:45:41
        '''
        def is_valid(nums):
            # using constraints to only check invalid cases
            only_nums = [n for n in nums if n != '.']
            return len(set(only_nums)) == len(only_nums)

        for row in board:
            if not is_valid(row):
                return False
        
        for col in zip(*board):
            if not is_valid(col):
                return False

        for i in range(3):
            for j in range(3):
                col_slice = slice(3*j, 3*(j+1)) # create reusable slice object 
                grid = board[3*i][col_slice] + board[3*i+1][col_slice] + board[3*i+2][col_slice]
                if not is_valid(grid):
                    return False
        
        return True


def is_valid(nums: List[str]):
    s = set(range(1, 10))
    for n in [int(x) for x in nums if x != "."]:
        if n in s:
            s.remove(n)
        else:
            return False
    return True


def get_subgrid(board, i, j):
    # We could do this manually one by one since there are only 3 rows.
    subgrid = []
    for m in range(3 * i, 3 * (i + 1)):
        subgrid += board[m][3 * j : 3 * (j + 1)]
    return subgrid

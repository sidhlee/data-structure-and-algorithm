"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:
'./rotate_image_1.jpg'

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
'./rotate_image_2.jpg'

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

Do not return anything, modify matrix in-place instead.
"""

from typing import List


class Solution:
    def rotate_diagonal_swap_and_reverse(self, matrix: List[List[int]]) -> None:
        """
        2022-06-20T11:17:27.787Z
        Runtime: 39 ms (85%)
        Memory Usage: 13.9 MB (74%)

        col -> row
        30 -> 00, 20 -> 01, 10 -> 01, 00 -> 03
        inplace -> swap?
        1 2 3 4
        5 6 7 8
        9 101112
        13141516
        swap across diagonal
        1 5 9 13
        2 6 1014
        3 7 11 15
        4 8 12 16
        then reverse each row
        """

        def d_swap(m, n):
            t = matrix[m][n]
            matrix[m][n] = matrix[n][m]
            matrix[n][m] = t

        for i in range(len(matrix)):
            # don't swap already swapped
            for j in range(i + 1, len(matrix)):
                d_swap(i, j)

        for row in matrix:
            row.reverse()

    def rotate_pythonic_swap(self, matrix: List[List[int]]) -> None:
        """
        2022-06-20T11:35:04.495Z
        Runtime: 55 ms (42%)
        Memory Usage: 13.9 MB (74%)
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                # if i != j: -> this check might not be worth it since we have the upper bound of 20 x 20
                # it might actually be faster to skip the check for all the rest
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for row in matrix:
            row.reverse()

    def rotate_one_liner(self, matrix: List[List[int]]) -> None:
        """
        2022-06-20T12:25:12.613Z

        Runtime: 63 ms (24%)
        Memory Usage: 13.9 MB (74%)

        1. use slicing with negative step for reversing the rows
        2. then use zip to turn columns into rows

        It's more intuitive to go from 2 -> 1, but it will take iteration through rows to reverse columns.

        Try visualizing from 1 to 2. row reverse then diagonal flip (it's easier to see if you flip first)

        Remember that reverse and transpose can have different orders and have the same result!

        123     789     741
        456 ->  456 ->  852
        789     123     963

        123     147     741
        456 ->  258 ->  852
        789     369     963

        ** This solution returns a list of tuples because * operator spreads iterator into tuples.

        """
        matrix[:] = zip(*matrix[::-1])

    def rotate_one_liner_2(self, matrix: List[List[int]]) -> None:
        """
        2022-08-19 08:37:21
        Runtime: 39 ms (89%)
        Memory Usage: 13.8 MB (75%)

        matrix will be a list a tuple eg. [(1,2), (3, 4), ..], but passes the test
        reversed is faster than matrix[::-1] & more readable
        """
        matrix[:] = zip(*reversed(matrix))

    def rotate_return_list(self, matrix: List[List[int]]) -> None:
        """
        2022-06-25T21:34:19.603Z
        Runtime: 34 ms
        Memory Usage: 13.9 MB

        This solution returns a list though many testers will not check the type.
        consider skipping mapping mapping.

        * zip always returns tuples

        123 147 741
        456 258 852
        789 369 963

        123 789 741
        456 456 851
        789 123 963

        >>> nums[:] = zip([1, 2, 3], [2, 3, 4])
        >>> nums
        [(1, 2), (2, 3), (3, 4)]
        """
        matrix.reverse()
        matrix[:] = list(map(list, zip(*matrix)))

    def rotate_reverse_once(self, matrix: List[List[int]]) -> None:
        """
         1 2 3     9 6 3    7 4 1
         4 5 6 ->  8 5 2 -> 8 5 2
         7 8 9     7 4 1    9 6 3

        '9'2 3    9 2 3    9'6'3
         4 5 6 ->'8'5 6 -> 8 5 2
         7 8'1'   7'4'1    7 4 1

         0,0 <-> 2,2
         0,1 <-> 1,2
         2,2 <-> 2,2

         1,0 <-> 2,1
         1,1 <-> 1,1
         1,2 <-> 0,1

         Rotate the array across reversed diagonal (/)
         Then only 1 reverse is required to get to the desired formation.
        """
        l = len(matrix)
        for c in range(l - 1):
            for r in range(l - 1 - c):
                matrix[r][c], matrix[l - c - 1][l - r - 1] = (
                    matrix[l - c - 1][l - r - 1],
                    matrix[r][c],
                )
        matrix.reverse()

    def rotate_reverse_and_zip_and_map_to_list(self, matrix: List[List[int]]) -> None:
        '''
        2022-10-16 16:25:53
        '''
        matrix[:] = map(list, zip(*matrix[::-1]))

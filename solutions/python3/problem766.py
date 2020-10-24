# -*- coding: utf-8 -*-
"""
766. Toeplitz Matrix

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load
at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""


class Solution:
    def isToeplitzMatrix(self, matrix):
        row_count = len(matrix)
        col_count = len(matrix[0])

        # first row
        for col_ind, base_val in enumerate(matrix[0]):
            cur_col = col_ind + 1
            cur_row = 1
            while cur_col < col_count and cur_row < row_count:
                if matrix[cur_row][cur_col] != base_val:
                    return False

                cur_col += 1
                cur_row += 1

        for row_ind, row in enumerate(matrix):
            col_ind = 0
            base_val = row[0]
            cur_col = 1
            cur_row = row_ind + 1

            while cur_col < col_count and cur_row < row_count:
                if matrix[cur_row][cur_col] != base_val:
                    return False

                cur_col += 1
                cur_row += 1

        return True

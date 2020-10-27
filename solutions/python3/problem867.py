# -*- coding: utf-8 -*-
"""
867. Transpose Matrix

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""


class Solution:
    def transpose(self, matrix):
        row_count = len(matrix)
        col_count = len(matrix[0])

        res = []
        for col in range(col_count):
            one_col = []
            for row in range(row_count):
                one_col.append(matrix[row][col])
            res.append(one_col)

        return res

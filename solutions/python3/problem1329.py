# -*- coding: utf-8 -*-
"""
1329. Sort the Matrix Diagonally

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and
going in the bottom-right direction until reaching the matrix's end.
For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0],
mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""


class Solution:
    def diagonalSort(self, mat):
        row_count = len(mat)
        col_count = len(mat[0])
        for row in range(row_count):
            self._update_diag(mat, row_count, col_count, row, 0)

        for col in range(1, col_count):
            self._update_diag(mat, row_count, col_count, 0, col)

        return mat

    def _update_diag(self, mat, row_max, col_max, row, col):
        indexes = []
        values = []
        while row < row_max and col < col_max:
            indexes.append([row, col])
            values.append(mat[row][col])
            row += 1
            col += 1

        for index, value in zip(indexes, sorted(values)):
            mat[index[0]][index[1]] = value


# -*- coding: utf-8 -*-
"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Constraints:
matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        i_max = length // 2

        if length % 2:
            j_max = i_max + 1
        else:
            j_max = i_max

        for i in range(i_max):
            for j in range(j_max):
                i_tmp = int(length - 1 - i)
                j_tmp = int(length - 1 - j)

                matrix[j][i_tmp], matrix[i_tmp][j_tmp], matrix[j_tmp][i], matrix[i][j] = \
                    matrix[i][j], matrix[j][i_tmp], matrix[i_tmp][j_tmp], matrix[j_tmp][i]

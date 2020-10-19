# -*- coding: utf-8 -*-
"""
1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal
that are not part of the primary diagonal.

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""


class Solution:
    def diagonalSum(self, mat) -> int:
        res = 0
        end_ind = len(mat) - 1
        for ind, arr in enumerate(mat):
            if ind == end_ind:
                res += arr[ind]
            else:
                res += arr[ind] + arr[end_ind]

            end_ind -= 1

        return res

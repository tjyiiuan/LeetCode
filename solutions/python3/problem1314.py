# -*- coding: utf-8 -*-
"""
1314. Matrix Block Sum

Given a m * n matrix mat and an integer K,
return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c]
for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
"""
class Solution:
    def matrixBlockSum(self, mat, K):
        if K == 0:
            return mat

        for i, i_list in enumerate(mat):
            for j, _ in enumerate(i_list):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    mat[i][j] += mat[i][j - 1]
                elif j == 0:
                    mat[i][j] += mat[i - 1][j]
                else:
                    mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]

        res = []
        for r in range(i + 1):
            l = []
            r_min = max(r - K, 0)
            r_max = min(r + K, i)
            for c in range(j + 1):
                c_min = max(c - K, 0)
                c_max = min(c + K, j)

                if r_min == 0 and c_min == 0:
                    l.append(mat[r_max][c_max])
                elif r_min == 0:
                    l.append(mat[r_max][c_max] - mat[r_max][c_min - 1])
                elif c_min == 0:
                    l.append(mat[r_max][c_max] - mat[r_min - 1][c_max])
                else:
                    l.append(mat[r_max][c_max] - mat[r_min - 1][c_max] - mat[r_max][c_min - 1] + mat[r_min - 1][c_min - 1])
            res.append(l)

        return res

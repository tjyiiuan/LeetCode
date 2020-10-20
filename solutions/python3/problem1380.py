# -*- coding: utf-8 -*-
"""
1380. Lucky Numbers in a Matrix

Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
"""


class Solution:
    def luckyNumbers(self, matrix):
        res = []

        l_row = len(matrix)
        l_col = len(matrix[0])
        col_max_cache = {}
        for col_ind in range(l_col):
            col = [row[col_ind] for row in matrix]
            row_pre = -float("inf")
            row_ind = -1
            for r_ind, val in enumerate(col):
                if val > row_pre:
                    row_pre = val
                    row_ind = r_ind

            if row_ind not in col_max_cache:
                col_max_cache[row_ind] = {row_pre}
            else:
                col_max_cache[row_ind].add(row_pre)

        for row_ind, row in enumerate(matrix):
            if row_ind not in col_max_cache:
                continue

            row_min = min(row)
            if row_min in col_max_cache[row_ind]:
                res.append(row_min)

        return res

# -*- coding: utf-8 -*-
"""
1582. Special Positions in a Binary Matrix
Easy

147

6

Add to List

Share
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Constraints:

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is 0 or 1.
"""


class Solution:
    def numSpecial(self, mat):
        res = 0
        row_count = len(mat)
        for cur_row_ind, row in enumerate(mat):
            if sum(row) != 1:
                continue

            col_ind = row.index(1)
            valid = True
            for row_ind in range(row_count):
                if row_ind == cur_row_ind:
                    continue

                if mat[row_ind][col_ind] == 1:
                    valid = False
                    break

            if valid:
                res += 1

        return res

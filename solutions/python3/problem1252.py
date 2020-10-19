# -*- coding: utf-8 -*-
"""
1252. Cells with Odd Values in a Matrix

Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices
where indices[i] = [ri, ci].
For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

Constraints:

1 <= n <= 50
1 <= m <= 50
1 <= indices.length <= 100
0 <= indices[i][0] < n
0 <= indices[i][1] < m
"""


class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        res_mat = [[0] * m for i in range(n)]
        for ri, ci in indices:
            for r_ind, row in enumerate(res_mat):
                if r_ind == ri:
                    row = [val + 1 for val in row]

                row[ci] += 1
                res_mat[r_ind] = row

        res = 0
        for row in res_mat:
            for val in row:
                if val % 2 == 1:
                    res += 1

        return res

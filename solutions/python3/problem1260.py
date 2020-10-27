# -*- coding: utf-8 -*-
"""
1260. Shift 2D Grid

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
"""


class Solution:
    def shiftGrid(self, grid, k):
        row_count = len(grid)
        col_count = len(grid[0])
        shift_row = (k // col_count) % row_count
        k = k % col_count

        if shift_row:
            grid = grid[-shift_row:] + grid[:-shift_row]

        if k == 0:
            return grid
        res = [[0] * col_count for row in range(row_count)]
        for row in range(row_count):
            for col in range(col_count):
                new_col = col + k
                if new_col >= col_count:
                    new_col = new_col % col_count
                    new_row = (row + 1) % row_count
                else:
                    new_row = row
                res[new_row][new_col] = grid[row][col]

        return res

# -*- coding: utf-8 -*-
"""
463. Island Perimeter

You are given row x col grid representing a map
where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
"""


class Solution:
    def islandPerimeter(self, grid):
        max_row_ind = len(grid) - 1
        max_col_ind = len(grid[0]) - 1
        res = 0

        for row_ind, row in enumerate(grid):
            for col_ind, val in enumerate(row):
                if val == 0:
                    continue
                # left
                if col_ind == 0 or row[col_ind - 1] != 1:
                    res += 1

                # right
                if col_ind == max_col_ind or row[col_ind + 1] != 1:
                    res += 1

                # up
                if row_ind == 0 or grid[row_ind - 1][col_ind] != 1:
                    res += 1

                # down
                if row_ind == max_row_ind or grid[row_ind + 1][col_ind] != 1:
                    res += 1

        return res

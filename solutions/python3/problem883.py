# -*- coding: utf-8 -*-
"""
883. Projection Area of 3D Shapes

On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

Note:

1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 50
"""


class Solution:
    def projectionArea(self, grid):
        res = 0
        for row in grid:
            max_row = 0
            for val in row:
                if val == 0:
                    continue
                res += 1  # top
                max_row = max(max_row, val)
            res += max_row  # by row

        col_count = len(grid[0])
        res += sum(max(row[ind] for row in grid) for ind in range(col_count))  # by column

        return res

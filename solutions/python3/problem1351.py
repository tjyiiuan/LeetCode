# -*- coding: utf-8 -*-
"""
1351. Count Negative Numbers in a Sorted Matrix

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""


class Solution:
    def countNegatives(self, grid) -> int:
        res = 0
        for row in grid:
            for val in row:
                if val < 0:
                    res += 1

        return res

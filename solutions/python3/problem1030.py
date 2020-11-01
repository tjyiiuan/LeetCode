# -*- coding: utf-8 -*-
"""
1030. Matrix Cells in Distance Order

We are given a matrix with R rows and C columns has cells with integer coordinates (r, c),
where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0)
from smallest distance to largest distance.
Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.
(You may return the answer in any order that satisfies this condition.)

Note:

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C
"""


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        cache = {}
        for row in range(R):
            for col in range(C):
                diff = abs(row - r0) + abs(col - c0)
                if diff not in cache:
                    cache[diff] = [[row, col]]
                else:
                    cache[diff].append([row, col])

        res = []
        for diff, point_list in sorted(cache.items()):
            res.extend(point_list)

        return res

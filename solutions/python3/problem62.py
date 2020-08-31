# -*- coding: utf-8 -*-
"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    cache[i][j] = 1
                else:
                    cache[i][j] = cache[i - 1][j] + cache[i][j - 1]

        return cache[m - 1][n - 1]
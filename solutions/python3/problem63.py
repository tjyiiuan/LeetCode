# -*- coding: utf-8 -*-
"""
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        for i, i_list in enumerate(obstacleGrid):
            for j, num in enumerate(i_list):
                if num == 1:
                    continue

                if i == 0 and j == 0:
                    obstacleGrid[i][j] = -1
                elif i == 0:
                    if obstacleGrid[i][j - 1] >= 0:
                        obstacleGrid[i][j] = 0
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                elif j == 0:
                    if obstacleGrid[i - 1][j] >= 0:
                        obstacleGrid[i][j] = 0
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                else:
                    if obstacleGrid[i - 1][j] < 0:
                        obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                    if obstacleGrid[i][j - 1] < 0:
                        obstacleGrid[i][j] += obstacleGrid[i][j - 1]

        if obstacleGrid[i][j] >= 0:
            return 0
        else:
            return -obstacleGrid[i][j]

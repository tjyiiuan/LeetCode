# -*- coding: utf-8 -*-
"""
1266. Minimum Time Visiting All Points

On a plane there are n points with integer coordinates points[i] = [xi, yi].
Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally
(it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.

Constraints:

points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
"""


class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        res = 0
        last_point_x, last_point_y = points[0]
        for xi, yi in points[1:]:
            res += max(abs(last_point_x - xi), abs(last_point_y - yi))
            last_point_x, last_point_y = xi, yi

        return res

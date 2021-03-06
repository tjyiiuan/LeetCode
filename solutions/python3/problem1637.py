# -*- coding: utf-8 -*-
"""
1637. Widest Vertical Area Between Two Points Containing No Points

Given n points on a 2D plane where points[i] = [xi, yi],
Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height).
The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Constraints:

n == points.length
2 <= n <= 105
points[i].length == 2
0 <= xi, yi <= 109
"""


class Solution:
    def maxWidthOfVerticalArea(self, points):
        x_axis = sorted(set(point[0] for point in points))
        return max(x_axis[ind] - x_axis[ind - 1] for ind in range(1, len(x_axis)))

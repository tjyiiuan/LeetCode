# -*- coding: utf-8 -*-
"""
1828. Queries on Number of Points Inside a Circle

You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane.
Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a
radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are
considered inside.

Return an array answer, where answer[j] is the answer to the jth query.


Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 500
1 <= queries.length <= 500
queries[j].length == 3
0 <= xj, yj <= 500
1 <= rj <= 500
All coordinates are integers.

"""


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for x, y, radius in queries:
            count = 0
            radius_sq = radius * radius
            for point in points:
                if pow(point[0] - x, 2) + pow(point[1] - y, 2) <= radius_sq:
                    count += 1
            result.append(count)

        return result

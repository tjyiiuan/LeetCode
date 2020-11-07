# -*- coding: utf-8 -*-
"""
1496. Path Crossing

Given a string path, where path[i] = 'N', 'S', 'E' or 'W',
each representing moving one unit north, south, east, or west, respectively.
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is,
if at any time you are on a location you've previously visited.
Return False otherwise.

Constraints:

1 <= path.length <= 10^4
path will only consist of characters in {'N', 'S', 'E', 'W}
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        path_set = {(0, 0)}

        for char in path:
            if char == "N":
                x += 1
            elif char == "S":
                x -= 1
            elif char == "E":
                y -= 1
            elif char == "W":
                y += 1

            if (x, y) in path_set:
                return True
            path_set.add((x, y))

        return False

# -*- coding: utf-8 -*-
"""
1051. Height Checker

Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students
to be standing in non-decreasing order of height.

Notice that when a group of students is selected they can reorder in any possible way
between themselves and the non selected students remain on their seats.

Constraints:

1 <= heights.length <= 100
1 <= heights[i] <= 100
"""


class Solution:
    def heightChecker(self, heights) -> int:
        res = 0
        target = sorted(heights)

        for tar, hei in zip(target, heights):
            if tar != hei:
                res += 1

        return res

# -*- coding: utf-8 -*-
"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""


class Solution:
    def trap(self, height):
        if not height:
            return 0

        res = 0
        r_max_list = []
        last_max = -1

        for j in height[::-1]:
            if j > last_max:
                last_max = j

            r_max_list.insert(0, last_max)

        left_max = -1

        for ind, i in enumerate(height):
            if i > left_max:
                left_max = i

            res += min(r_max_list[ind], left_max) - i

        return res

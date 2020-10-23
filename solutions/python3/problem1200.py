# -*- coding: utf-8 -*-
"""
1200. Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference
of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

Constraints:

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
"""


class Solution:
    def minimumAbsDifference(self, arr):
        sorted_arr = sorted(arr)
        res = []
        diff = float("inf")
        for ind, val in enumerate(sorted_arr[1:], start=1):
            cur_diff = val - sorted_arr[ind - 1]
            if cur_diff == diff:
                res.append([sorted_arr[ind - 1], val])
            elif cur_diff < diff:
                diff = cur_diff
                res = [[sorted_arr[ind - 1], val]]

        return res

# -*- coding: utf-8 -*-
"""
1619. Mean of Array After Removing Some Elements

Given an integer array arr, return the mean of the remaining integers after removing the smallest 5%
and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.

Constraints:

20 <= arr.length <= 1000
arr.length is a multiple of 20.
0 <= arr[i] <= 105
"""


class Solution:
    def trimMean(self, arr):
        ind = int(len(arr) * 0.05)
        length = 18 * ind
        return sum(sorted(arr)[ind: - ind]) / length

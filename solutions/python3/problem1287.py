# -*- coding: utf-8 -*-
"""
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs
more than 25% of the time.

Return that integer.

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""


class Solution:
    def findSpecialInteger(self, arr):
        occur = len(arr) / 4
        count = 0
        last = -1
        for val in arr:
            if val == last:
                count += 1
            else:
                last = val
                count = 1

            if count > occur:
                return val

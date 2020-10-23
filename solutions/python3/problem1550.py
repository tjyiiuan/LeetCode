# -*- coding: utf-8 -*-
"""
1550. Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array.
Otherwise, return false.

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""


class Solution:
    def threeConsecutiveOdds(self, arr):
        length = 0
        last = False
        for val in arr:
            if val % 2 == 0:
                length = 0
                last = False
            elif last:
                length += 1
                if length == 3:
                    return True
            else:
                length = 1
                last = True

        return length >= 3

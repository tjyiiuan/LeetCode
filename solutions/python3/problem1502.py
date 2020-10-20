# -*- coding: utf-8 -*-
"""
1502. Can Make Arithmetic Progression From Sequence

Given an array of numbers arr. A sequence of numbers is called an arithmetic progression
if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

Constraints:

2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
"""


class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        sorted_arr = sorted(arr)
        diff = sorted_arr[1] - sorted_arr[0]
        for ind in range(2, len(arr)):
            if sorted_arr[ind] - sorted_arr[ind - 1] != diff:
                return False

        return True

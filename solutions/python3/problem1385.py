# -*- coding: utf-8 -*-
"""
1385. Find the Distance Value Between Two Arrays

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j]
where |arr1[i]-arr2[j]| <= d.

Constraints:

1 <= arr1.length, arr2.length <= 500
-10^3 <= arr1[i], arr2[j] <= 10^3
0 <= d <= 100
"""


class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        res = 0
        for val1 in arr1:
            valid = True
            for val2 in arr2:
                if abs(val1 - val2) <= d:
                    valid = False
                    break
            if valid:
                res += 1

        return res

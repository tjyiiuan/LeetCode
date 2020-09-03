# -*- coding: utf-8 -*-
"""
69. Sqrt(x)
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res

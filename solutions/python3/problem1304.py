# -*- coding: utf-8 -*-
"""
1304. Find N Unique Integers Sum up to Zero

Given an integer n, return any array containing n unique integers such that they add up to 0.

Constraints:

1 <= n <= 1000
"""


class Solution:
    def sumZero(self, n):
        if n % 2 == 1:
            return self.sumZero(n - 1) + [0]
        else:
            res = []
            for i in range(1, n // 2 + 1):
                res.append(i)
                res.append(-i)
        return res

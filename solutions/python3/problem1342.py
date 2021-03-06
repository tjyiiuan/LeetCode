# -*- coding: utf-8 -*-
"""
1342. Number of Steps to Reduce a Number to Zero

Given a non-negative integer num, return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Constraints:

0 <= num <= 10^6
"""


class Solution:
    def numberOfSteps (self, num: int) -> int:
        res = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            res += 1

        return res

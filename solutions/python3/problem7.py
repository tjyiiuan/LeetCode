# -*- coding: utf-8 -*-
"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            b_neg = True
            x = -x
            num_thres = 2 ** 31
        else:
            b_neg = False
            num_thres = 2 ** 31 - 1

        res = 0
        while x > 0:
            tmp = x % 10
            if res > ((num_thres - tmp) / 10):
                return 0

            res = res * 10 + tmp
            x = x // 10

        if b_neg:
            return -res
        else:
            return res

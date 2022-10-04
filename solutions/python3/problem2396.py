# -*- coding: utf-8 -*-
"""
2396. Strictly Palindromic Number

An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of
the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.


Constraints:

4 <= n <= 105
"""


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            # convert by base
            num = n
            digits = []
            while num != 0:
                res = num % base
                digits.append(res)
                num = num // base

            # is palindromic
            if digits != digits[::-1]:
                return False

        return True

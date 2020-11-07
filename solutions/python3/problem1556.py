# -*- coding: utf-8 -*-
"""
1556. Thousand Separator

Given an integer n, add a dot (".") as the thousands separator and return it in string format.

Constraints:

0 <= n < 2^31
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = ""
        str_n = str(n)
        count = 0
        ind = len(str_n) - 1
        while ind >= 0:
            count += 1
            if count == 4:
                res = "." + res
                count = 1
            res = str_n[ind] + res
            ind -= 1

        return res

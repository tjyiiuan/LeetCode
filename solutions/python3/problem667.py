# -*- coding: utf-8 -*-
"""
667. Beautiful Arrangement II

Given two integers n and k, you need to construct a list which contains n different positive integers
ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|]
has exactly k distinct integers.

If there are multiple answers, print any of them.

Note:
The n and k are in the range 1 <= k < n <= 104.
"""


class Solution:
    def constructArray(self, n: int, k: int):
        res = list(range(1, n + 1))
        ind = 1
        while k > 1:
            res[ind:] = res[ind:][::-1]
            ind += 1
            k -= 1

        return res

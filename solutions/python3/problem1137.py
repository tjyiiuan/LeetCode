# -*- coding: utf-8 -*-
"""
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        tribo_list = [0, 1, 1]
        ind = 2
        while ind < n:
            tribo_list.append(sum(tribo_list[-3:]))
            ind += 1

        return tribo_list[n]

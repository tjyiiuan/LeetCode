# -*- coding: utf-8 -*-
"""
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Note:

0 ≤ N ≤ 30.
"""


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1

        n2 = 0
        n1 = 1

        N -= 2
        while N > 0:
            N -= 1
            n2, n1 = n1, n2 + n1

        return n2 + n1

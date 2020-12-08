# -*- coding: utf-8 -*-
"""
1134. Armstrong Number

The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.

Note:

1 <= N <= 10^8
"""


class Solution:
    def isArmstrong(self, num) -> bool:
        length = len(str(num))

        return num == sum(int(i) ** length for i in str(num))

# -*- coding: utf-8 -*-
"""
1281. Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Constraints:

1 <= n <= 10^5
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        nsum = 0
        while n > 0:
            num = n % 10
            n = n // 10
            prod *= num
            nsum += num

        return prod - nsum

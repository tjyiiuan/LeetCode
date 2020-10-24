# -*- coding: utf-8 -*-
"""
1399. Count Largest Group

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.

Return how many groups have the largest size.

Constraints:

1 <= n <= 10^4
"""


class Solution:
    def countLargestGroup(self, n: int) -> int:
        cache = {}
        for val in range(1, n + 1):
            count_val = self._count(val)
            if count_val not in cache:
                cache[count_val] = 1
            else:
                cache[count_val] += 1

        max_size = 0
        group_count = 0
        for count_val, count in cache.items():
            if count == max_size:
                group_count += 1
            elif count > max_size:
                max_size = count
                group_count = 1

        return group_count

    def _count(self, number):
        res = 0
        while number > 0:
            res += number % 10
            number = number // 10

        return res

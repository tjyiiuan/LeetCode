# -*- coding: utf-8 -*-
"""
2220. Minimum Bit Flips to Convert Number

A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to
0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not
shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101,
flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.


Constraints:

0 <= start, goal <= 109
"""


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        start_digits = self._convert_to_base(start)
        goal_digits = self._convert_to_base(goal)
        length = max(len(start_digits), len(goal_digits))
        for i in range(length):
            if self._get_digit(start_digits, i) != self._get_digit(goal_digits, i):
                count += 1

        return count

    def _convert_to_base(self, num, base=2):
        digits = []
        while num != 0:
            res = num % base
            digits.append(res)
            num = num // base

        return digits

    def _get_digit(self, digits, index):
        if index >= len(digits):
            return 0
        else:
            return digits[index]

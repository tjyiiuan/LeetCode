# -*- coding: utf-8 -*-
"""
1323. Maximum 69 Number

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Constraints:

1 <= num <= 10^4
num's digits are 6 or 9.
"""


class Solution:
    def maximum69Number (self, num: int) -> int:
        res = list(str(num))
        for ind, val in enumerate(res):
            if val == "6":
                res[ind] = "9"
                break

        return int("".join(res))

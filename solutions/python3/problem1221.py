# -*- coding: utf-8 -*-
"""
1221. Split a String in Balanced Strings

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Constraints:

1 <= s.length <= 1000
s[i] = 'L' or 'R'
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        count = 0
        for char in s:
            if char == "R":
                count += 1
            else:
                count -= 1
            if count == 0:
                res += 1

        return res

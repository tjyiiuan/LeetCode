# -*- coding: utf-8 -*-
"""
171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for char in s:
            res = res * 26 + ord(char) - ord("A") + 1

        return res

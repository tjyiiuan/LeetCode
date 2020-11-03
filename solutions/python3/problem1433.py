# -*- coding: utf-8 -*-
"""
1433. Check If a String Can Break Another String

Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of
string s2 or vice-versa. In other words s2 can break s1 or vice-versa.

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.
=
Constraints:

s1.length == n
s2.length == n
1 <= n <= 10^5
All strings consist of lowercase English letters.
"""


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_char = sorted(s1)
        s2_char = sorted(s2)
        order = None

        for ind, char in enumerate(s1_char):
            if char == s2_char[ind]:
                continue
            elif order is None:
                order = char > s2_char[ind]
            else:
                if (char > s2_char[ind]) != order:
                    return False

        return True

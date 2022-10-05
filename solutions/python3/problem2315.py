# -*- coding: utf-8 -*-
"""
2315. Count Asterisks

You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters, vertical bars '|', and asterisks '*'.
s contains an even number of vertical bars '|'.
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        pair = False
        count = 0
        for char in s:
            if char == "*" and not pair:
                count += 1
            elif char == "|":
                pair = not pair

        return count

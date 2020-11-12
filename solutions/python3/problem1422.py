# -*- coding: utf-8 -*-
"""
1422. Maximum Score After Splitting a String

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings
(i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones
in the right substring.

Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
"""


class Solution:
    def maxScore(self, s: str) -> int:
        l_score = 1 - int(s[0])
        r_score = s[1:].count("1")

        res = l_score + r_score
        cur_score = res

        for char in s[1:-1]:
            if char == "1":
                cur_score -= 1
            else:
                cur_score += 1
            res = max(res, cur_score)

        return res

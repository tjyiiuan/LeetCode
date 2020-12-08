# -*- coding: utf-8 -*-
"""
1180. Count Substrings with Only One Distinct Letter

Given a string S, return the number of substrings that have only one distinct letter.

Constraints:

1 <= S.length <= 1000
S[i] consists of only lowercase English letters.
"""


class Solution:
    def countLetters(self, string: str) -> int:
        last_char = ""
        cur_count = 0
        res = 0
        for char in string:
            if char != last_char:
                res += cur_count * (cur_count + 1) // 2
                cur_count = 1
                last_char = char
            else:
                cur_count += 1

        res += cur_count * (cur_count + 1) // 2
        return res

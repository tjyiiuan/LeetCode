# -*- coding: utf-8 -*-
"""
1309. Decrypt String from Alphabet to Integer Mapping

Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Constraints:

1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.
"""


class Solution:
    def freqAlphabets(self, string: str) -> str:
        max_ind = len(string) - 1
        last_ind = len(string) - 3
        ind = 0
        res = ""
        while ind <= max_ind:
            if ind > last_ind:
                char_ind = int(string[ind])
                ind += 1
            elif string[ind + 2] == "#":
                char_ind = int(string[ind:ind + 2])
                ind += 3
            else:
                char_ind = int(string[ind])
                ind += 1
            res += chr(ord('a') + char_ind - 1)

        return res

# -*- coding: utf-8 -*-
"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        len_com_max = min(len(i) for i in strs)
        len_com = 0
        while len_com < len_com_max:
            if len(set(i[len_com] for i in strs)) == 1:
                len_com += 1
            else:
                break

        return strs[0][:len_com]

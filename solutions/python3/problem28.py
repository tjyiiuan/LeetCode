# -*- coding: utf-8 -*-
"""
28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Constraints:
haystack and needle consist only of lowercase English characters.
"""


class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        h_ind = 0
        n_ind = 0
        h_len = len(haystack)
        n_len = len(needle)

        while h_ind < h_len and n_ind < n_len:
            if haystack[h_ind] == needle[n_ind]:
                h_ind += 1
                n_ind += 1
            else:
                h_ind = h_ind - n_ind + 1
                n_ind = 0

        if n_ind == n_len:
            return h_ind - n_ind
        else:
            return -1

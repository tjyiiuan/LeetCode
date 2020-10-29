# -*- coding: utf-8 -*-
"""
763. Partition Labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible
so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""


class Solution:
    def partitionLabels(self, string):
        cache = {}
        for ind, char in enumerate(string):
            if char not in cache:
                cache[char] = [ind, ind]
            else:
                cache[char][1] = ind

        res_ind = []
        this_start = -1
        this_end = -1
        for char in cache:
            start_ind, end_ind = cache[char]
            if start_ind > this_end:
                res_ind.append((this_start, this_end))
                this_start = start_ind
                this_end = end_ind
            else:
                this_end = max(end_ind, this_end)

        res_ind.append((this_start, this_end))

        return [end_ind - start_ind + 1 for start_ind, end_ind in res_ind[1:]]

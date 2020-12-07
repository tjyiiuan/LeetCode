# -*- coding: utf-8 -*-
"""
760. Find Anagram Mappings

Given two lists A and B, and B is an anagram of A.
B is an anagram of A means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.

Note:

A, B have equal lengths in range [1, 100].
A[i], B[i] are integers in range [0, 10^5].
"""


class Solution:
    def anagramMappings(self, a_array, b_array):
        cache = {}
        for index, val in enumerate(b_array):
            if val not in cache:
                cache[val] = [index]
            else:
                cache[val].append(index)

        return [cache[val].pop() for val in a_array]

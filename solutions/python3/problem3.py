# -*- coding: utf-8 -*-
"""
3. Longest Substring Without Repeating Characters
Medium

10405

604

Add to List

Share
Given a string, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        cache = {}
        res = 0
        k = -1
        for ind, char in enumerate(s):
            if char in cache and cache[char] > k:
                k = cache[char]
                cache[char] = ind
            else:
                cache[char] = ind
                res = max(res, ind - k)

        return res

# -*- coding: utf-8 -*-
"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""


class Solution:
    def groupAnagrams(self, strs):
        res = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)

            if key not in res:
                res[key] = []

            res[key].append(s)

        return res.values()

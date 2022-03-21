# -*- coding: utf-8 -*-
"""
1347. Minimum Number of Steps to Make Two Strings Anagram

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with
another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Constraints:

1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_dict = {}

        for char in s:
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] += 1

        for char in t:
            if char not in char_dict:
                char_dict[char] = 0

            char_dict[char] -= 1

        return sum(abs(i) for _, i in char_dict.items()) // 2

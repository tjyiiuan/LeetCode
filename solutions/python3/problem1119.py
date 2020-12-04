# -*- coding: utf-8 -*-
"""
1119. Remove Vowels from a String

Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.


Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
"""


class Solution:
    def removeVowels(self, string: str) -> str:
        res = []
        vowel_set = {"a", "e", "i", "o", "u"}
        for char in string:
            if char not in vowel_set:
                res.append(char)

        return "".join(res)

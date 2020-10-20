# -*- coding: utf-8 -*-
"""
1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""


class Solution:
    def countCharacters(self, words, chars: str) -> int:
        res = 0
        char_cache = self._count_char(chars)
        for word in words:
            word_char = self._count_char(word)
            b_valid = True
            for char, count in word_char.items():
                if char not in char_cache:
                    b_valid = False
                    break
                elif char_cache[char] < word_char[char]:
                    b_valid = False
                    break

            if b_valid:
                res += len(word)

        return res

    def _count_char(self, word):
        cache = {}
        for char in word:
            if char not in cache:
                cache[char] = 1
            else:
                cache[char] += 1

        return cache

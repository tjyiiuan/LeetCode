# -*- coding: utf-8 -*-
"""
1408. String Matching in an Array

Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to
left and/or right side of words[j].

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.
"""


class Solution:
    def stringMatching(self, words):
        sorted_words = sorted(words, key=lambda x: len(x))
        res = []
        for ind, word in enumerate(sorted_words):
            for word2 in sorted_words[ind + 1:]:
                if word in word2:
                    res.append(word)
                    break
        return res

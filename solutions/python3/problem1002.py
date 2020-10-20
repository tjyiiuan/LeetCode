# -*- coding: utf-8 -*-
"""
1002. Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters
that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times,
you need to include that character three times in the final answer.

You may return the answer in any order.

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""


class Solution:
    def commonChars(self, arr):
        word_list = []
        for word in arr:
            char_list = [0] * 26
            for char in word:
                char_list[ord(char) - ord('a')] += 1
            word_list.append(char_list)

        res = []
        for ind, word_count in enumerate(zip(*word_list)):
            min_count = min(word_count)
            for i in range(min_count):
                res.append(chr(ord('a') + ind))

        return res

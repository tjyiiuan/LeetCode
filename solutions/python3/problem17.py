# -*- coding: utf-8 -*-
"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution:
    def __init__(self):
        self.cache = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letterCombinations(self, digits):
        length = len(digits)
        if length == 0:
            return []

        res = [""]
        for i in digits:
            res = [i + j for j in self.cache[i] for i in res]

        return res

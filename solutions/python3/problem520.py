# -*- coding: utf-8 -*-
"""
520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        def is_cap(char):
            return char.upper() == char

        if not is_cap(word[0]):
            if is_cap(word[1]):
                return False
            must_cap = False
        elif is_cap(word[1]):
            must_cap = True
        else:
            must_cap = False

        for letter in word[2:]:
            if is_cap(letter) ^ must_cap:
                return False

        return True

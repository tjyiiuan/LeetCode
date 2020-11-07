# -*- coding: utf-8 -*-
"""
1417. Reformat The String

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit
is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""


class Solution:
    def reformat(self, s: str) -> str:
        num_set = set(str(i) for i in range(10))
        digit_cache = ""
        letter_chace = ""
        for char in s:
            if char in num_set:
                digit_cache += char
            else:
                letter_chace += char

        res = ""
        digit_length = len(digit_cache)
        letter_length = len(letter_chace)
        if digit_length == letter_length:
            for ind in range(letter_length):
                res += digit_cache[ind]
                res += letter_chace[ind]
        elif digit_length == letter_length + 1:
            for ind in range(letter_length):
                res += digit_cache[ind]
                res += letter_chace[ind]
            res += digit_cache[-1]
        elif digit_length + 1 == letter_length:
            for ind in range(digit_length):
                res += letter_chace[ind]
                res += digit_cache[ind]
            res += letter_chace[-1]

        return res

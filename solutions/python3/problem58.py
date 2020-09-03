# -*- coding: utf-8 -*-
"""
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = False
        count = 0
        ind = len(s) - 1
        while ind >= 0:
            char = s[ind]
            if char == " ":
                if last_word:
                    return count
            else:
                last_word = True
                count += 1

            ind -= 1

        return count

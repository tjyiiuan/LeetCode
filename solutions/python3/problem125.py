# -*- coding: utf-8 -*-
"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Constraints:
s consists only of printable ASCII characters.
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def isPalindrome(self, s):
        ind1 = 0
        ind2 = len(s) - 1

        while ind1 < ind2:
            o1 = self.get_ord(s[ind1])
            o2 = self.get_ord(s[ind2])

            if o1 == -1:
                ind1 += 1
            elif o2 == -1:
                ind2 -= 1
            elif o1 != o2:
                return False
            else:
                ind1 += 1
                ind2 -= 1

        return True

    def get_ord(self, char):
        if char not in self.cache:
            o = ord(char)
            if 48 <= o <= 57:
                self.cache[char] = o
            elif 97 <= o <= 122:
                self.cache[char] = o
            elif 65 <= o <= 90:
                self.cache[char] = o + 32
            else:
                self.cache[char] = -1

        return self.cache[char]

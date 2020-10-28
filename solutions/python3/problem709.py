# -*- coding: utf-8 -*-
"""
709. To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""


class Solution:
    def toLowerCase(self, string) -> str:
        res = ""
        for char in string:
            if ord("z") >= ord(char) >= ord("a"):
                res += char
            elif ord("Z") >= ord(char) >= ord("A"):
                res += chr(ord(char) - ord("A") + ord("a"))
            else:
                res += char

        return res

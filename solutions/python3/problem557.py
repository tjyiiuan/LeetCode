# -*- coding: utf-8 -*-
"""
557. Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""



class Solution:
    def reverseWords(self, string: str) -> str:
        return " ".join([s[::-1] for s in string.split()])

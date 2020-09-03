# -*- coding: utf-8 -*-
"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def __init__(self):
        self.cache = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

    def isValid(self, s: str) -> bool:
        res = [""]
        for char in s:
            if char in self.cache:
                res.append(self.cache[char])
            else:
                if res.pop() == char:
                    continue
                else:
                    return False

        return res == [""]

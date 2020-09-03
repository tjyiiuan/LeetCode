# -*- coding: utf-8 -*-
"""
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up:

Could you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False
        else:
            tmp = 0
            while x > tmp:
                tmp = tmp * 10 + x % 10
                x = x // 10

            return x == tmp or x == tmp // 10

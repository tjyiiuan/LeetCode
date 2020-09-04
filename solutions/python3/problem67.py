# -*- coding: utf-8 -*-
"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Constraints:
Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""


class Solution:
    def addBinary(self, a, b):
        res = ""
        head = 0
        ind_a = len(a) - 1
        ind_b = len(b) - 1

        while ind_a >= 0 and ind_b >= 0:
            tmp = int(a[ind_a]) + int(b[ind_b]) + head
            if tmp >= 2:
                head = 1
                tmp = tmp % 2
            else:
                head = 0

            res = str(tmp) + res
            ind_a -= 1
            ind_b -= 1

        if ind_a >= 0:
            ind = ind_a
            binary = a
        else:
            ind = ind_b
            binary = b

        while ind >= 0:
            tmp = int(binary[ind]) + head
            if tmp >= 2:
                head = 1
                tmp = tmp % 2
            else:
                head = 0

            res = str(tmp) + res
            ind -= 1

        if head == 1:
            res = "1" + res

        return res

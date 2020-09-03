# -*- coding: utf-8 -*-
"""
66. Plus One

Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.


Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""


class Solution:
    def plusOne(self, digits):
        res = []
        ind = len(digits) - 1
        head = 0
        digits[-1] += 1

        while ind >= 0:
            digit = digits[ind]
            digit += head

            if digit >= 10:
                head = 1
                digit = digit % 10
            else:
                head = 0

            res.insert(0, digit)
            ind -= 1

        if head == 1:
            res.insert(0, 1)

        return res

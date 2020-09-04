# -*- coding: utf-8 -*-
"""
8. String to Integer (atoi)
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
 no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""


class Solution:
    def myAtoi(self, strs):
        strs = strs.split()
        if not strs:
            return 0
        else:
            strs = strs[0]

        num = 0
        int_max = 2 ** 31 - 1
        must_digit = False
        neg_digit = False
        is_digit = False

        for char in strs:
            if char in "0123456789":
                is_digit = True
                digit = int(char)
                if (int_max - digit) / 10 < num:
                    # overflow
                    num = int_max
                    break
                else:
                    num = num * 10 + digit
            else:
                if must_digit:
                    break
                elif char == "-":
                    if is_digit:
                        break
                    else:
                        int_max = 2 ** 31
                        neg_digit = True
                        must_digit = True
                elif char == "+":
                    if is_digit:
                        break
                    else:
                        must_digit = True
                else:
                    break

        if neg_digit:
            return -num
        else:
            return num

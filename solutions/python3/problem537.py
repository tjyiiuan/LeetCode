# -*- coding: utf-8 -*-
"""
537. Complex Number Multiplication

Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi,
where the integer a and b will both belong to the range of [-100, 100].
And the output should be also in this form.
"""


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_split = a.split("+")
        if len(a_split) == 1:
            if a[-1] == "i":
                real_a, imag_a = 0, int(a[:-1])
            else:
                real_a, imag_a = int(a), 0
        else:
            real_a, imag_a = a_split
            real_a = int(real_a)
            imag_a = int(imag_a[:-1])

        b_split = b.split("+")
        if len(b_split) == 1:
            if b[-1] == "i":
                real_b, imag_b = 0, int(b[:-1])
            else:
                real_b, imag_b = int(b), 0
        else:
            real_b, imag_b = b_split
            real_b = int(real_b)
            imag_b = int(imag_b[:-1])

        real_part = real_a * real_b - imag_a * imag_b
        imag_part = imag_a * real_b + real_a * imag_b

        return f"{real_part}+{imag_part}i"

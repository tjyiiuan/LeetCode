# -*- coding: utf-8 -*-
"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (not s) or (numRows < 2) or (len(s) <= numRows):
            return s

        res = [""] * numRows
        offset = 2 * numRows - 2
        for ind, char in enumerate(s):
            res_ind = ind % offset
            if res_ind < numRows:
                res[res_ind] += char
            else:
                res[offset - res_ind] += char

        return "".join(res)

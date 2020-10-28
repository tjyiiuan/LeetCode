# -*- coding: utf-8 -*-
"""
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""


class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        elif numRows == 3:
            return [[1], [1, 1], [1, 2, 1]]
        elif numRows == 4:
            return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        elif numRows == 5:
            return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        elif numRows == 6:
            return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
        else:
            res = self.generate(6)
            numRows -= 6
            while numRows > 0:
                last_row = res[-1]
                tmp_row = [last_row[ind] + last_row[ind - 1] for ind in range(1, len(last_row))]
                res.append([1] + tmp_row + [1])
                numRows -= 1
            return res

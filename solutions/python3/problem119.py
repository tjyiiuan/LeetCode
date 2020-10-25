# -*- coding: utf-8 -*-
"""
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

Constraints:

0 <= rowIndex <= 40
"""


class Solution:
    def getRow(self, row_index):
        if row_index == 0:
            return [1]
        elif row_index == 1:
            return [1, 1]
        elif row_index == 2:
            return [1, 2, 1]
        elif row_index == 3:
            return [1, 3, 3, 1]
        elif row_index == 4:
            return [1, 4, 6, 4, 1]
        elif row_index == 5:
            return [1, 5, 10, 10, 5, 1]

        last_row = self.getRow(row_index - 1)
        tmp_row = [last_row[ind] + last_row[ind - 1] for ind in range(1, len(last_row))]
        return [1] + tmp_row + [1]

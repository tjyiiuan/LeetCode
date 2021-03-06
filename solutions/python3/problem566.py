# -*- coding: utf-8 -*-
"""
566. Reshape the Matrix

In MATLAB, there is a very useful function called 'reshape',
which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array,
and two positive integers r and c representing the row number and column number of the wanted reshaped matrix,
respectively.

The reshaped matrix need to be filled with all the elements of the original matrix
in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix;
Otherwise, output the original matrix.

Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""


class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        all_num = []
        for row in nums:
            all_num.extend(row)

        if len(all_num) != r * c:
            return nums

        start_ind = 0
        res = []
        for ind in range(r):
            res.append(all_num[start_ind:start_ind + c])
            start_ind += c

        return res

# -*- coding: utf-8 -*-
"""
931. Minimum Falling Path Sum

Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's column by at most one.

Constraints:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""


class Solution:
    def minFallingPathSum(self, A):
        length = len(A)
        if length == 1:
            return min(A[0])

        for i in range(1, length):
            for j in range(length):
                A[i][j] += min(A[i - 1][max(0, j - 1): j + 2])

        return min(A[-1])

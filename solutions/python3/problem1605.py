# -*- coding: utf-8 -*-
"""
1605. Find Valid Matrix Given Row and Column Sums

You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the
ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the
elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum
requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that
fulfills the requirements exists.


Constraints:

1 <= rowSum.length, colSum.length <= 500
0 <= rowSum[i], colSum[i] <= 108
sum(rows) == sum(columns)
"""


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row_count = len(rowSum)
        col_count = len(colSum)
        result = []
        for i in range(row_count):
            row_sum = rowSum[i]
            row = []
            for j in range(col_count):
                col_sum = colSum[j]
                col = min(row_sum, col_sum)
                row.append(col)
                row_sum -= col
                colSum[j] -= col

            result.append(row)

        return result

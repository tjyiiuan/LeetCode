# -*- coding: utf-8 -*-
"""
1337. The K Weakest Rows in a Matrix

Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians),
return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j,
or they have the same number of soldiers but i is less than j.
Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""


class Solution:
    def kWeakestRows(self, mat, k):
        cache = []
        for ind, row in enumerate(mat):
            count = 0
            for val in row:
                if val == 0:
                    break
                count += val
            cache.append((count, ind))

        return [ind for _, ind in sorted(cache)[:k]]

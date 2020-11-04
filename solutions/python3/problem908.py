# -*- coding: utf-8 -*-
"""
908. Smallest Range I

Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""


class Solution:
    def smallestRangeI(self, A, K):
        diff = max(A) - min(A) - 2 * K
        if diff < 0:
            return 0
        else:
            return diff

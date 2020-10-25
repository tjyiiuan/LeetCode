# -*- coding: utf-8 -*-
"""
1013. Partition Array Into Three Parts With Equal Sum

Given an array A of integers, return true if and only if we can partition the array
into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with
(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Constraints:

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4
"""


class Solution:
    def canThreePartsEqualSum(self, arr):
        for ind in range(1, len(arr)):
            arr[ind] = arr[ind] + arr[ind - 1]

        arr_sum = arr[-1]
        if arr_sum % 3 != 0:
            return False

        arr_sum1 = arr_sum // 3
        arr_sum2 = arr_sum1 * 2

        try:
            first_ind = arr.index(arr_sum1)
        except ValueError:
            return False

        try:
            second_ind = arr[first_ind + 1:-1].index(arr_sum2)
        except ValueError:
            return False

        return True

# -*- coding: utf-8 -*-
"""

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""


class Solution:
    def sortArrayByParityII(self, arr):
        odd_arr = []
        even_arr = []
        for val in arr:
            if val % 2 == 1:
                odd_arr.append(val)
            else:
                even_arr.append(val)

        res = []
        for odd, even in zip(odd_arr, even_arr):
            res.append(even)
            res.append(odd)

        return res

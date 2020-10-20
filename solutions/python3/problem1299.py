# -*- coding: utf-8 -*-
"""
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""


class Solution:
    def replaceElements(self, arr):
        res = [-1]

        pre = -float("inf")
        for val in arr[::-1]:
            if val > pre:
                pre = val
            res.append(pre)

        return res[::-1][1:]

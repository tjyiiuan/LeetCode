# -*- coding: utf-8 -*-
"""
1588. Sum of All Odd Length Subarrays

Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000
"""


class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        res = 0
        max_ind = len(arr) - 1
        for length in range(1, len(arr) + 1, 2):
            for ind, val in enumerate(arr):
                start = max(0, ind - length + 1)
                end = min(ind, max_ind - length + 1)
                res += val * (end - start + 1)

        return res

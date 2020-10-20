# -*- coding: utf-8 -*-
"""
977. Squares of a Sorted Array

Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted non-decreasing order.
"""

class Solution:
    def sortedSquares(self, arr):
        return sorted(i ** 2 for i in arr)

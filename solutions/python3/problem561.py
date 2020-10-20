# -*- coding: utf-8 -*-
"""
561. Array Partition I

Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""


class Solution:
    def arrayPairSum(self, nums):
        res = 0
        for i, val in enumerate(sorted(nums)):
            if i % 2 == 0:
                res += val

        return res

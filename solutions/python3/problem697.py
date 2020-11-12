# -*- coding: utf-8 -*-
"""
697. Degree of an Array

Given a non-empty array of non-negative integers nums,
the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""


class Solution:
    def findShortestSubArray(self, nums):
        cache = {}
        for ind, val in enumerate(nums):
            if val not in cache:
                cache[val] = [ind]
            else:
                cache[val].append(ind)

        degree = 0
        res = 0
        for indices in cache.values():
            if len(indices) > degree:
                degree = len(indices)
                res = indices[-1] - indices[0] + 1
            elif len(indices) == degree:
                res = min(indices[-1] - indices[0] + 1, res)

        return res

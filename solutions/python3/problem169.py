# -*- coding: utf-8 -*-
"""
169. Majority Element

Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution:
    def majorityElement(self, nums):
        major_count = len(nums) / 2
        cache = {}
        for val in nums:
            if val not in cache:
                cache[val] = 1
            else:
                cache[val] += 1

        for val, count in cache.items():
            if count > major_count:
                return val

# -*- coding: utf-8 -*-
"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


class Solution:
    def twoSum(self, nums, target):
        cache = {}
        for ind, i in enumerate(nums):
            res = target - i
            if res in cache:
                return [cache[res], ind]
            else:
                cache[i] = ind

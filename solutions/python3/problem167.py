# -*- coding: utf-8 -*-
"""
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Constraints:
2 <= nums.length <= 3 * 104
-1000 <= nums[i] <= 1000
nums is sorted in increasing order.
-1000 <= target <= 1000
"""


class Solution:
    def twoSum(self, numbers, target):
        cache = {}

        for index, val in enumerate(numbers, start=1):
            res = target - val
            if res in cache:
                return [cache[res], index]
            else:
                cache[val] = index

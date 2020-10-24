# -*- coding: utf-8 -*-
"""
1413. Minimum Value to Get Positive Step by Step Sum

Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""


class Solution:
    def minStartValue(self, nums):
        for ind in range(1, len(nums)):
            nums[ind] = nums[ind] + nums[ind - 1]

        min_val = min(nums)
        if min_val > 0:
            return 1
        else:
            return 1 - min_val

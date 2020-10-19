# -*- coding: utf-8 -*-
"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""


class Solution:
    def runningSum(self, nums):
        if len(nums) > 1:
            for ind, val in enumerate(nums[1:], start=1):
                nums[ind] = val + nums[ind - 1]

        return nums

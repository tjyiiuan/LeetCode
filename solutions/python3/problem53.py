# -*- coding: utf-8 -*-
"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])

        return max(nums)

# -*- coding: utf-8 -*-
"""
198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.



Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def rob(self, nums):
        if not nums:
            return 0

        length = len(nums)
        if length not in self.cache:
            if length <= 2:
                result = max(nums)
            else:
                result = max(self.rob(nums[:-1]), self.rob(nums[:-2]) + nums[-1])

            self.cache[length] = result

        return self.cache[length]

# -*- coding: utf-8 -*-
"""
665. Non-decreasing Array

Given an array nums with n integers, your task is to check if it could become non-decreasing
by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Constraints:

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
"""


class Solution:
    def checkPossibility(self, nums):
        ind_set = set()
        for ind in range(1, len(nums)):
            if nums[ind] - nums[ind - 1] < 0:
                ind_set.add(ind)

        if not ind_set:
            return True
        elif len(ind_set) > 1:
            return False
        else:
            wrong_ind = ind_set.pop()
            if wrong_ind == 1 or wrong_ind == len(nums) - 1:
                return True
            else:
                return nums[wrong_ind] >= nums[wrong_ind - 2] or nums[wrong_ind + 1] >= nums[wrong_ind - 1]

# -*- coding: utf-8 -*-
"""
1295. Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""


class Solution:
    def findNumbers(self, nums) -> int:
        res = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                res += 1

        return res

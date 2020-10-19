# -*- coding: utf-8 -*-
"""
1464. Maximum Product of Two Elements in an Array

Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3
"""


class Solution:
    def maxProduct(self, nums) -> int:
        if nums[0] < nums[1]:
            cache = (nums[0], nums[1])
        else:
            cache = (nums[1], nums[0])

        for num in nums[2:]:
            if num > cache[1]:
                cache = [cache[1], num]
            elif num > cache[0]:
                cache = [num, cache[1]]

        return (cache[0] - 1) * (cache[1] - 1)

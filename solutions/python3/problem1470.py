# -*- coding: utf-8 -*-
"""
1470. Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Constraints:

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
"""


class Solution:
    def shuffle(self, nums, n: int):
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])

        return res

# -*- coding: utf-8 -*-
"""
303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""
class NumArray:

    def __init__(self, nums):
        self.nums = [0]
        for i in range(len(nums)):
            self.nums.append(self.nums[i] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j + 1] - self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
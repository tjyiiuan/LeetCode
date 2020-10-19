# -*- coding: utf-8 -*-
"""
1389. Create Target Array in the Given Order

Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Constraints:

1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i
"""


class Solution:
    def createTargetArray(self, nums, index):
        res = []
        for ind, num in zip(index, nums):
            res.insert(ind, num)

        return res

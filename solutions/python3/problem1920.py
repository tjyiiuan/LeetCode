# -*- coding: utf-8 -*-
"""
1920. Build Array from Permutation

Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]]
for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
The elements in nums are distinct.


Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?
"""


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]

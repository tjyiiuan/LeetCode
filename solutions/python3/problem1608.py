# -*- coding: utf-8 -*-
"""
1608. Special Array With X Elements Greater Than or Equal X

You are given an array nums of non-negative integers.
nums is considered special if there exists a number x such that there are exactly x numbers in nums that are
greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1.
It can be proven that if nums is special, the value for x is unique.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""


class Solution:
    def specialArray(self, nums):
        nums = sorted(nums)
        if nums[0] >= len(nums):
            return len(nums)

        for count in range(1, len(nums)):
            if nums[-count] >= count > nums[-count - 1]:
                return count

        return -1

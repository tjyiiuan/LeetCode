"""
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""


class Solution:
    def searchInsert(self, nums, target):
        for ind, num in enumerate(nums):
            if num > target:
                return ind
            elif num == target:
                return ind
            else:
                continue

        return len(nums)

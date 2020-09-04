# -*- coding: utf-8 -*-
"""
26. Remove Duplicates from Sorted Array

Given a sorted array nums,
remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        length = len(nums)
        ind = 1
        last_val = nums[0]

        while ind < length:
            if nums[ind] == last_val:
                nums.pop(ind)
                length -= 1
            else:
                last_val = nums[ind]
                ind += 1

        return length

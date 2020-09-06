# -*- coding: utf-8 -*-
"""
80. Remove Duplicates from Sorted Array II

Given a sorted array nums,
remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        length = len(nums)
        ind = 1
        count = 1
        last_val = nums[0]

        while ind < length:
            if nums[ind] == last_val:
                if count == 2:
                    nums.pop(ind)
                    length -= 1
                else:
                    ind += 1
                    count += 1
            else:
                last_val = nums[ind]
                ind += 1
                count = 1

        return length

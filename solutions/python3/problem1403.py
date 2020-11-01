# -*- coding: utf-8 -*-
"""
1403. Minimum Subsequence in Non-Increasing Order

Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than
the sum of the non included elements in such subsequence.

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions,
return the subsequence with the maximum total sum of all its elements.
A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.

Note that the solution with the given constraints is guaranteed to be unique.
Also return the answer sorted in non-increasing order.

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 100
"""


class Solution:
    def minSubsequence(self, nums):
        half_sum = sum(nums) / 2
        sorted_nums = sorted(nums)
        ind = len(nums) - 1
        res = []
        cur_sum = 0
        while ind >= 0:
            res.append(sorted_nums[ind])
            cur_sum += sorted_nums[ind]
            if cur_sum > half_sum:
                return res
            ind -= 1

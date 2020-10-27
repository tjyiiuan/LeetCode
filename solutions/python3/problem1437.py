# -*- coding: utf-8 -*-
"""
1437. Check If All 1's Are at Least Length K Places Away

Given an array nums of 0s and 1s and an integer k,
return True if all 1's are at least k places away from each other, otherwise return False.

Constraints:

1 <= nums.length <= 10^5
0 <= k <= nums.length
nums[i] is 0 or 1
"""


class Solution:
    def kLengthApart(self, nums, k):
        if k == 0:
            return True

        last_ind = - k - 1
        for ind, val in enumerate(nums):
            if val != 1:
                continue
            elif ind - last_ind <= k:
                return False
            else:
                last_ind = ind

        return True

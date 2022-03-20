# -*- coding: utf-8 -*-
"""
2006. Count Number of Pairs With Absolute Difference K

Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that
|nums[i] - nums[j]| == k.

The value of |x| is defined as:
    x if x >= 0.
    -x if x < 0.

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
1 <= k <= 99
"""


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        num_dict = {}
        for i in nums:
            if i not in num_dict:
                num_dict[i] = 0
            num_dict[i] += 1

        result = 0
        for i in nums:
            result += num_dict.get(i - k, 0)
            result += num_dict.get(i + k, 0)

        return result // 2

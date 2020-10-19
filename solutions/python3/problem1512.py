# -*- coding: utf-8 -*-
"""
1512. Number of Good Pairs

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


class Solution:
    def numIdenticalPairs(self, nums) -> int:
        cache = {}
        for val in nums:
            if val not in cache:
                cache[val] = 1
            else:
                cache[val] += 1

        res = 0
        for val, count in cache.items():
            res += count * (count - 1) // 2

        return res

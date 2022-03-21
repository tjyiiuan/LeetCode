# -*- coding: utf-8 -*-
"""
2176. Count Equal and Divisible Pairs in an Array

Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where
0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

Constraints:

1 <= nums.length <= 100
1 <= nums[i], k <= 100
"""


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        num_dict = {}
        for index, value in enumerate(nums):
            if value not in num_dict:
                num_dict[value] = []
            num_dict[value].append(index)

        result = 0
        for _, index in num_dict.items():
            count = len(index)
            if count < 2:
                continue

            for ind, i in enumerate(index[:-1]):
                for j in index[ind + 1:]:
                    if i * j % k == 0:
                        result += 1

        return result

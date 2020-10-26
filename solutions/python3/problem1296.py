# -*- coding: utf-8 -*-
"""
1296. Divide Array in Sets of K Consecutive Numbers

Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
"""


class Solution:
    def isPossibleDivide(self, nums, k: int) -> bool:
        if k == 1:
            return True

        if len(nums) % k != 0:
            return False

        cache = {}
        group_count = len(nums) // k
        for val in nums:
            if val not in cache:
                cache[val] = 1
            else:
                cache[val] += 1

        for key in sorted(cache.keys()):
            cur_count = cache[key]
            if cur_count == 0:
                continue
            elif cur_count > group_count or cur_count < 0:
                return False

            group_count -= cur_count
            for i in range(k):
                if key + i not in cache:
                    return False
                cache[key + i] -= cur_count

        return True

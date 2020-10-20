# -*- coding: utf-8 -*-
"""
1460. Make Two Arrays Equal by Reversing Sub-arrays

Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it.
You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.

Constraints:

target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
"""


class Solution:
    def canBeEqual(self, target, arr) -> bool:
        cache = {}
        for val in target:
            if val not in cache:
                cache[val] = 1
            else:
                cache[val] += 1

        for val in arr:
            if val not in cache:
                return False
            cache[val] -= 1

        for val, count in cache.items():
            if count != 0:
                return False

        return True

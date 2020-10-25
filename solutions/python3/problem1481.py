# -*- coding: utf-8 -*-
"""
1481. Least Number of Unique Integers after K Removals

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""


class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        cache = {}
        for num in arr:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1

        res = len(cache)
        for count in sorted(cache.values()):
            if k > count:
                k -= count
                res -= 1
            elif k == count:
                return res - 1
            else:
                return res

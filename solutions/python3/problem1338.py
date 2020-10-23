# -*- coding: utf-8 -*-
"""
1338. Reduce Array Size to The Half

Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Constraints:

1 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
"""


class Solution:
    def minSetSize(self, arr) -> int:
        cache = {}
        for val in arr:
            if val not in cache:
                cache[val] = 1
            else:
                cache[val] += 1

        cur_count = 0
        res = 0
        tar_size = len(arr) / 2
        for count in sorted(cache.values())[::-1]:
            res += 1
            cur_count += count
            if cur_count >= tar_size:
                return res

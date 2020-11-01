# -*- coding: utf-8 -*-
"""
1207. Unique Number of Occurrences

Given an array of integers arr,
write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""


class Solution:
    def uniqueOccurrences(self, arr):
        cache = {}
        for val in arr:
            if val not in cache:
                cache[val] = 1
            else:
                cache[val] += 1

        occur_list = list(cache.values())

        return len(occur_list) == len(set(occur_list))

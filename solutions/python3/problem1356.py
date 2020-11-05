# -*- coding: utf-8 -*-
"""
1356. Sort Integers by The Number of 1 Bits

Given an integer array arr.
You have to sort the integers in the array in ascending order by the number of 1's in their binary representation
and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 10^4
"""


class Solution:
    def sortByBits(self, arr):
        cache = {}
        for val in sorted(arr):
            count = sum(int(i) for i in bin(val)[2:])
            if count not in cache:
                cache[count] = [val]
            else:
                cache[count].append(val)

        res = []
        for _, val in sorted(cache.items()):
            res.extend(val)

        return res

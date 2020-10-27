# -*- coding: utf-8 -*-
"""
769. Max Chunks To Make Sorted

Given an array arr that is a permutation of [0, 1, ..., arr.length - 1],
we split the array into some number of "chunks" (partitions), and individually sort each chunk.
After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Note:

arr will have length in range [1, 10].
arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
"""


class Solution:
    def maxChunksToSorted(self, arr):
        res = 0
        max_ind = len(arr) - 1
        target_ind = arr.index(0)
        cur_ind = 0

        while True:
            if arr[cur_ind] > target_ind:
                target_ind = arr[cur_ind]
                cur_ind += 1
            elif cur_ind == target_ind:
                res += 1
                cur_ind += 1
                if cur_ind > max_ind:
                    return res
                target_ind = arr.index(cur_ind)
            else:
                cur_ind += 1

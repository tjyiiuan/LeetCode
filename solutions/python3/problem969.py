# -*- coding: utf-8 -*-
"""
969. Pancake Sorting

Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[1...k].
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1],
so arr = [1,2,3,4] after the pancake flip at k = 3.

Return the k-values corresponding to a sequence of pancake flips that sort arr.
Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= arr.length
All integers in arr are unique (i.e. arr is a permutation of the integers from 1 to arr.length).
"""


class Solution:
    def pancakeSort(self, arr):
        res = []
        sorted_arr = sorted(arr)
        ind = len(arr) - 1
        while ind >= 0:
            if arr[ind] != sorted_arr[ind]:
                cur_index = arr.index(sorted_arr[ind])
                res.append(cur_index + 1)
                res.append(ind + 1)
                arr[:cur_index + 1] = arr[:cur_index + 1][::-1]
                arr[:ind + 1] = arr[:ind + 1][::-1]

            ind -= 1
        return res

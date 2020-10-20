# -*- coding: utf-8 -*-
"""
1122. Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
"""


class Solution:
    def relativeSortArray(self, arr1, arr2):
        cache = dict((val, []) for val in arr2)
        end = []
        for val in arr1:
            if val not in cache:
                end.append(val)
            else:
                cache[val].append(val)

        res = []
        for val, l in cache.items():
            res += l

        return res + sorted(end)


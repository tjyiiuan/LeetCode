# -*- coding: utf-8 -*-
"""
1213. Intersection of Three Sorted Arrays

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order,
return a sorted array of only the integers that appeared in all three arrays.

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""


class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        return sorted(set(arr1) & set(arr2) & set(arr3))


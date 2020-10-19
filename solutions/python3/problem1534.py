# -*- coding: utf-8 -*-
"""
1534. Count Good Triplets

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

Constraints:

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000
"""


class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        res = 0
        cache = {}
        length = len(arr)
        for i in range(0, length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if (i, j) not in cache:
                        cache[(i, j)] = abs(arr[i] - arr[j])

                    if (j, k) not in cache:
                        cache[(j, k)] = abs(arr[j] - arr[k])

                    if (i, k) not in cache:
                        cache[(i, k)] = abs(arr[i] - arr[k])

                    if cache[(i, j)] <= a and cache[(j, k)] <= b and cache[(i, k)] <= c:
                        res += 1
        return res

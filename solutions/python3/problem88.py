# -*- coding: utf-8 -*-
"""
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Constraints:
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[m + n + 1] = nums1[m]
                m -= 1
            else:
                nums1[m + n + 1] = nums2[n]
                n -= 1

        nums1[:n + 1] = nums2[:n + 1]

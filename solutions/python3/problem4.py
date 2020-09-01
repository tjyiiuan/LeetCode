# -*- coding: utf-8 -*-
"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively.

Return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).


Constraints:

nums1,length == m
nums2,length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        ind1 = 0
        ind2 = 0
        res = []
        length = len1 + len2

        while ind1 < len1 and ind2 < len2:
            diff = (ind1 + ind2) * 2 - length

            if nums1[ind1] > nums2[ind2]:
                current_val = nums2[ind2]
                ind2 += 1
            else:
                current_val = nums1[ind1]
                ind1 += 1

            if diff == -1:
                return current_val
            elif diff == -2 or diff == 0:
                res.append(current_val)
            elif diff > 0:
                return sum(res) / 2
            else:
                continue

        if ind1 >= len1:
            ind = ind2
            nums = nums2
            leng = len2
            cur_ind = ind1
        else:
            ind = ind1
            nums = nums1
            leng = len1
            cur_ind = ind2

        while ind < leng:
            diff = (cur_ind + ind) * 2 - length
            current_val = nums[ind]
            ind += 1

            if diff == -1:
                return current_val
            elif diff == -2 or diff == 0:
                res.append(current_val)
            elif diff > 0:
                return sum(res) / 2
            else:
                continue

        return sum(res) / 2

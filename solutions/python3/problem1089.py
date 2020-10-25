# -*- coding: utf-8 -*-
"""
1089. Duplicate Zeros

Given a fixed length array arr of integers, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""


class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr) - 1
        ind = 0
        while ind < length:
            if arr[ind] != 0:
                ind += 1
            else:
                arr[ind + 1:] = arr[ind: -1]
                ind += 2

        return

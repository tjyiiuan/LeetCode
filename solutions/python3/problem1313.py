# -*- coding: utf-8 -*-
"""
1313. Decompress Run-Length Encoded List

We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
For each such pair, there are freq elements with value val concatenated in a sublist.
Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

Constraints:

2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100
"""


class Solution:
    def decompressRLElist(self, nums):
        res = []
        for ind in range(0, len(nums), 2):
            res += [nums[ind + 1]] * nums[ind]

        return res

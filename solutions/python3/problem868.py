# -*- coding: utf-8 -*-
"""
868. Binary Gap

Given a positive integer n, find and return the longest distance between any two adjacent 1's
in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's).
The distance between two 1's is the absolute difference between their bit positions.
For example, the two 1's in "1001" have a distance of 3.

Constraints:

1 <= n <= 109
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        last_ind = None
        res = 0
        for ind, char in enumerate(bin(n)[2:]):
            if char == "1":
                if last_ind is None:
                    last_ind = ind
                else:
                    res = max(res, ind - last_ind)
                    last_ind = ind

        return res

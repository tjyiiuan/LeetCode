# -*- coding: utf-8 -*-
"""
986. Interval List Intersections

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty,
or can be represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""


class Solution:
    def intervalIntersection(self, A, B):
        res = []
        a_ind = 0
        a_length = len(A)
        b_ind = 0
        b_length = len(B)

        while a_ind < a_length and b_ind < b_length:
            a_start, a_end = A[a_ind]
            b_start, b_end = B[b_ind]
            if a_start > b_end:
                b_ind += 1
            elif b_start > a_end:
                a_ind += 1
            else:
                res.append([max(a_start, b_start), min(a_end, b_end)])
                if a_end < b_end:
                    a_ind += 1
                elif a_end > b_end:
                    b_ind += 1
                else:
                    a_ind += 1
                    b_ind += 1

        return res

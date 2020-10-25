# -*- coding: utf-8 -*-
"""
565. Array Nesting

A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

Note:

N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].
"""


class Solution:
    def arrayNesting(self, nums):
        all_set = set(range(len(nums)))
        res = 0

        this_ind = all_set.pop()
        one_set = {this_ind}
        this_ind = nums[this_ind]

        while all_set:
            if this_ind not in one_set:
                one_set.add(this_ind)
                all_set.remove(this_ind)
                this_ind = nums[this_ind]
            else:
                res = max(res, len(one_set))

                this_ind = all_set.pop()
                one_set = {this_ind}
                this_ind = nums[this_ind]

        return max(res, len(one_set))

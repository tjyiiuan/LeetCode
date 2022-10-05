# -*- coding: utf-8 -*-
"""
2161. Partition Array According to Given Pivot

You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions
are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the
jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj.
Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.

Return nums after the rearrangement.


Constraints:

1 <= nums.length <= 105
-106 <= nums[i] <= 106
pivot equals to an element of nums.
"""


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lt = []
        eq = []
        gt = []
        for num in nums:
            if num < pivot:
                lt.append(num)
            elif num > pivot:
                gt.append(num)
            else:
                eq.append(num)

        return lt + eq + gt

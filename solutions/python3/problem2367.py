# -*- coding: utf-8 -*-
"""
2367. Number of Arithmetic Triplets

You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is
an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.


Constraints:

3 <= nums.length <= 200
0 <= nums[i] <= 200
1 <= diff <= 50
nums is strictly increasing.
"""


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        diff_set = set()
        for i in range(1, len(nums)):
            num = nums[i]
            for j in range(i):
                if num - nums[j] == diff:
                    diff_set.add(i)
                    if j in diff_set:
                        count += 1

                    break

        return count

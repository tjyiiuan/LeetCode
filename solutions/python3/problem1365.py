# -*- coding: utf-8 -*-
"""
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        cache = {}
        for ind, val in enumerate(nums):
            if val not in cache:
                cache[val] = [ind]
            else:
                cache[val].append(ind)

        count = 0
        res = [0] * len(nums)
        for val, ind_list in sorted(cache.items()):
            for ind in ind_list:
                res[ind] = count

            count += len(ind_list)

        return res

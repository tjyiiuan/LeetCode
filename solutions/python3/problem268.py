# -*- coding: utf-8 -*-
"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""


class Solution:
    def missingNumber(self, nums):
        res = (len(nums) * (len(nums) + 1)) // 2
        for num in nums:
            res -= num

        return res

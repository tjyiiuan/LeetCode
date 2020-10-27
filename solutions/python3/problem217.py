# -*- coding: utf-8 -*-
"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums):
        val_set = set()
        for val in nums:
            if val in val_set:
                return True
            else:
                val_set.add(val)

        return False

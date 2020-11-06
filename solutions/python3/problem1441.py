# -*- coding: utf-8 -*-
"""
1441. Build an Array With Stack Operations

Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.

Constraints:

1 <= target.length <= 100
1 <= target[i] <= 100
1 <= n <= 100
target is strictly increasing.
"""


class Solution:
    def buildArray(self, target, n: int):
        cur_ind = 1
        res = []
        for val in target:
            if val > cur_ind:
                for ind in range(val - cur_ind):
                    res.append("Push")
                    res.append("Pop")
                res.append("Push")
                cur_ind = val + 1
            elif val == cur_ind:
                res.append("Push")
                cur_ind = val + 1

        return res

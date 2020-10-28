# -*- coding: utf-8 -*-
"""
1630. Arithmetic Subarrays

A sequence of numbers is called arithmetic if it consists of at least two elements,
and the difference between every two consecutive elements is the same.
More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r,
representing the m range queries, where the ith query is the range [l[i], r[i]].
All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... ,
nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

Constraints:

n == nums.length
m == l.length
m == r.length
2 <= n <= 500
1 <= m <= 500
0 <= l[i] < r[i] < n
-105 <= nums[i] <= 105
"""


class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        res = []
        for ind in range(len(l)):
            if r[ind] - l[ind] <= 1:
                res.append(True)
            else:
                sorted_arr = sorted(nums[l[ind]: r[ind] + 1])
                diff = sorted_arr[1] - sorted_arr[0]
                b_arithmetic = True
                for index in range(2, len(sorted_arr)):
                    if sorted_arr[index] - sorted_arr[index - 1] != diff:
                        b_arithmetic = False
                        break
                res.append(b_arithmetic)

        return res

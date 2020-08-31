# -*- coding: utf-8 -*-
"""
413. Arithmetic Slices

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.
"""


class Solution:
    def numberOfArithmeticSlices(self, A):
        length = len(A)
        if length < 3:
            return 0

        diff = [A[i] - A[i - 1] for i in range(1, length)]
        last_diff = diff[0]
        this_count = 1
        total_count = []
        for i in range(1, length - 1):
            if diff[i] == last_diff:
                this_count += 1
            else:
                total_count.append(this_count)
                last_diff = diff[i]
                this_count = 1

        total_count.append(this_count)

        num = 0
        for count in total_count:
            if count < 2:
                continue

            num += count * (count - 1) / 2

        return int(num)


s = Solution()
print(s.numberOfArithmeticSlices([1,2,3,4, 4, 3, 2, 1, 3, 5, 7, 9, 2, 4, 6, 7,8,9,10,11,13,15,17,19,21,27,33,39,45]))
# -*- coding: utf-8 -*-
"""
832. Flipping an Image

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0, 1, 1] results in [1, 0, 0].

Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
"""


class Solution:
    def flipAndInvertImage(self, A):
        def flipping(arr):
            return [1 - i for i in arr[::-1]]

        return [flipping(row) for row in A]

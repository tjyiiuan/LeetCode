# -*- coding: utf-8 -*-
"""
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Constraints:
1 <= n <= 19
"""


class Solution:
    cache = {
        0: 1,
        1: 1,
        2: 2,
        3: 5
    }

    def numTrees(self, n: int) -> int:
        if n not in self.cache:
            res = 0
            left = 0
            right = n - left - 1

            while True:
                if left > right:
                    break
                elif left == right:
                    res += self.numTrees(left) ** 2
                else:
                    res += 2 * self.numTrees(left) * self.numTrees(right)

                left += 1
                right -= 1

            self.cache[n] = res

        return self.cache[n]

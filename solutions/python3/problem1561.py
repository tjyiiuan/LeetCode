# -*- coding: utf-8 -*-
"""
1561. Maximum Number of Coins You Can Get

There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins which you can have.

Constraints:

3 <= piles.length <= 10^5
piles.length % 3 == 0
1 <= piles[i] <= 10^4
"""


class Solution:
    def maxCoins(self, piles):
        sorted_piles = sorted(piles)
        count = len(piles) // 3
        ind = len(piles) - 2
        res = 0

        while count > 0:
            res += sorted_piles[ind]
            ind -= 2
            count -= 1

        return res

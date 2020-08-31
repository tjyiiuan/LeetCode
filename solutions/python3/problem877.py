# -*- coding: utf-8 -*-
"""
877. Stone Game

Alex and Lee play a game with piles of stones.
There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.
The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.
Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.
This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""


class Solution:
    def stoneGame(self, piles) -> bool:
        return True


class SolutionDP:
    def __init__(self):
        self.cache = {}

    def stoneGame(self, piles) -> bool:
        return self.best_take(piles) > 0

    def best_take(self, p):
        key = tuple(p)

        if key not in self.cache:
            if len(p) == 2:
                self.cache[key] = abs(p[0] - p[1])
            else:
                self.cache[key] = max(p[0] - self.best_take(p[1:]),
                                      p[-1] - self.best_take(p[:-1]))

        return self.cache[key]


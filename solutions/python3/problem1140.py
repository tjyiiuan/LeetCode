# -*- coding: utf-8 -*-
"""
1140. Stone Game II

Alex and Lee continue their games with piles of stones.
There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones.

Alex and Lee take turns, with Alex starting first.
Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.
Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.


Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
Accepted
"""


class Solution:
    def __init__(self):
        self.cache = {}

    def stoneGameII(self, piles) -> int:
        return self.best_pick(piles, 1)

    def best_pick(self, p, M):
        key = (tuple(p), M)
        max_x = 2 * M
        if key not in self.cache:
            all_sum = sum(p)
            if len(p) <= max_x:
                self.cache[key] = all_sum
            else:
                max_pick = -1
                for x in range(1, max_x + 1):
                    this_pick = sum(p[:x]) + all_sum - self.best_pick(p[x:], max(x, M))
                    max_pick = max(this_pick, max_pick)

                self.cache[key] = max_pick

        return self.cache[key]

s = Solution()
print(s.stoneGameII([20, 7, 9, 4, 9, 20, 7, 9]))
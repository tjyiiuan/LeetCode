# -*- coding: utf-8 -*-
"""
1217. Minimum Cost to Move Chips to The Same Position
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position.
In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.

Return the minimum cost needed to move all the chips to the same position.

Constraints:

1 <= position.length <= 100
1 <= position[i] <= 10^9
"""


class Solution:
    def minCostToMoveChips(self, position):
        res_count = [0, 0]
        for pos in position:
            res_count[pos % 2] += 1

        return min(res_count)

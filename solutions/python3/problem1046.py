# -*- coding: utf-8 -*-
"""
1046. Last Stone Weight

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.
Suppose the stones have weights x and y with x <= y.
The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""


class Solution:
    def lastStoneWeight(self, stones):
        stones = sorted(stones)
        while len(stones) > 1:
            diff = stones[-1] - stones[-2]
            if diff == 0:
                stones = stones[:-2]
            else:
                stones = sorted(stones[:-2] + [diff])

        return 0 if not stones else stones[0]

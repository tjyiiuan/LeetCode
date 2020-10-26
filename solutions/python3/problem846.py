# -*- coding: utf-8 -*-
"""
846. Hand of Straights

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

Note: This question is the same as 1296.

Constraints:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""


class Solution:
    def isNStraightHand(self, nums, k: int) -> bool:
        if k == 1:
            return True

        if len(nums) % k != 0:
            return False

        cache = {}
        group_count = len(nums) // k
        for val in nums:
            if val not in cache:
                cache[val] = 1
            else:
                cache[val] += 1

        for key in sorted(cache.keys()):
            cur_count = cache[key]
            if cur_count == 0:
                continue
            elif cur_count > group_count or cur_count < 0:
                return False

            group_count -= cur_count
            for i in range(k):
                if key + i not in cache:
                    return False
                cache[key + i] -= cur_count

        return True

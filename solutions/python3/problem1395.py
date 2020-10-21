# -*- coding: utf-8 -*-
"""
1395. Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k])
where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5
"""


class Solution:
    def numTeams(self, rating) -> int:
        cache = {0: [0, 0, 0, 0]}  # left_greater, left_less, right_greater, right_less
        for ind, val in enumerate(rating[1:], start=1):
            cache[ind] = [0, 0, 0, 0]

            for l_ind, l_val in enumerate(rating[0: ind]):
                if l_val > val:
                    cache[l_ind][3] += 1
                    cache[ind][0] += 1
                else:
                    cache[l_ind][2] += 1
                    cache[ind][1] += 1

        res = 0
        for ind, val in cache.items():
            res += val[0] * val[3] + val[1] * val[2]

        return res

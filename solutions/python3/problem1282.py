# -*- coding: utf-8 -*-
"""
1282. Group the People Given the Group Size They Belong To

There are n people that are split into some unknown number of groups.
Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in.
For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group.
If there are multiple answers, return any of them.
It is guaranteed that there will be at least one valid solution for the given input.

Constraints:

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
"""


class Solution:
    def groupThePeople(self, groupSizes):
        cache = {}
        res = []
        for ind, size in enumerate(groupSizes):
            if size not in cache:
                cache[size] = [ind]
            else:
                cache[size].append(ind)

            if len(cache[size]) == size:
                res.append(cache[size])
                cache[size] = []

        return res

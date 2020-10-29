# -*- coding: utf-8 -*-
"""
830. Positions of Large Groups

In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end],
where start and end denote the start and end indices (inclusive) of the group.
In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.

Constraints:

1 <= s.length <= 1000
s contains lower-case English letters only.
"""


class Solution:
    def largeGroupPositions(self, s):
        res = []
        last_char = ""
        count = -1
        for ind, char in enumerate(s + "_"):
            if char == last_char:
                count += 1
            else:
                if count >= 3:
                    res.append([ind - count, ind - 1])

                last_char = char
                count = 1

        return res
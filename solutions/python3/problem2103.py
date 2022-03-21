# -*- coding: utf-8 -*-
"""
2103. Rings and Rods

There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0
to 9.

You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two
characters in rings forms a color-position pair that is used to describe each ring where:

The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the
rod labeled 2, and a blue ring placed onto the rod labeled 1.

Return the number of rods that have all three colors of rings on them.

Constraints:

rings.length == 2 * n
1 <= n <= 100
rings[i] where i is even is either 'R', 'G', or 'B' (0-indexed).
rings[i] where i is odd is a digit from '0' to '9' (0-indexed).
"""


class Solution:
    def countPoints(self, rings: str) -> int:
        rod_dict = {}
        for i in range(len(rings) // 2):
            if rings[2 * i + 1] not in rod_dict:
                rod_dict[rings[2 * i + 1]] = set()

            rod_dict[rings[2 * i + 1]].add(rings[2 * i])

        result = 0
        for rod, r in rod_dict.items():
            if len(r) == 3:
                result += 1

        return result

# -*- coding: utf-8 -*-
"""
771. Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones : str) -> int:
        j_set = set(jewels)
        res = 0
        for s in stones:
            if s in j_set:
                res += 1

        return res

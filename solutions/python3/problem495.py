# -*- coding: utf-8 -*-
"""
495. Teemo Attacking

In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition.
Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point,
and makes Ashe be in poisoned condition immediately.

Note:

You may assume the length of given time series array won't exceed 10000.
You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking
are non-negative integers, which won't exceed 10,000,000.
"""


class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        dur = duration - 1
        last_end = -1
        res = 0
        for val in timeSeries:
            new_end = val + dur
            res += duration
            if val <= last_end:
                res -= last_end - val + 1

            last_end = new_end

        return res

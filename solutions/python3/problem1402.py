# -*- coding: utf-8 -*-
"""
1402. Reducing Dishes

A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  time[i]*satisfaction[i]

Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.


Constraints:

n == satisfaction.length
1 <= n <= 500
-10^3 <= satisfaction[i] <= 10^3
"""


class Solution:
    def maxSatisfaction(self, satisfaction) -> int:
        last_sum = 0
        sati = 0
        for i in sorted(satisfaction)[::-1]:
            tmp = last_sum + i
            if tmp >= 0:
                dl.insert(0, i)
                last_sum = tmp
                sati += tmp
        return sati

# -*- coding: utf-8 -*-
"""
983. Minimum Cost For Tickets

In a country popular for train travel, you have planned some train travelling one year in advance.
The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.
For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
"""


class Solution:
    def mincostTickets(self, days, costs) -> int:
        cache = [0] * (days[-1] + 1)
        today = 0
        for i in range(1, days[-1] + 1):
            if days[today] == i:
                today += 1
                cache[i] = min([cache[max(0, i - 1)] + costs[0],
                                cache[max(0, i - 7)] + costs[1],
                                cache[max(0, i - 30)] + costs[2]])
            else:
                cache[i] = cache[i - 1]

        return cache[-1]

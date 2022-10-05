# -*- coding: utf-8 -*-
"""
2391. Minimum Amount of Time to Collect Garbage

You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith
house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass
garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i
to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck
starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other
two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.


Constraints:

2 <= garbage.length <= 105
garbage[i] consists of only the letters 'M', 'P', and 'G'.
1 <= garbage[i].length <= 10
travel.length == garbage.length - 1
1 <= travel[i] <= 100
"""


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        collect_dict = {
            "G": False,
            "P": False,
            "M": False
        }
        minute_dict = {
            "G": 0,
            "P": 0,
            "M": 0
        }

        for i in range(len(travel), 0, -1):
            self._collect(garbage[i], collect_dict, minute_dict)
            travel_time = travel[i - 1]
            for key in ["G", "P", "M"]:
                if collect_dict[key]:
                    minute_dict[key] += travel_time
        self._collect(garbage[0], collect_dict, minute_dict)

        return sum(v if collect_dict[k] else 0 for k, v in minute_dict.items())

    def _collect(self, garbage, collect_dict, minute_dict):
        for char in garbage:
            collect_dict[char] = True
            minute_dict[char] += 1

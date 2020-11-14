# -*- coding: utf-8 -*-
"""
1184. Distance Between Bus Stops

A bus has n stops numbered from 0 to n - 1 that form a circle.
We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number
i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.

Constraints:

1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4
"""


class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        all_distance = sum(distance)
        s, e = sorted([start, destination])
        one_distance = sum(distance[s:e])
        return min(one_distance, all_distance - one_distance)

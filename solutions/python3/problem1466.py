# -*- coding: utf-8 -*-
"""
1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel
between two different cities (this network form a tree). Last year, The ministry of transport decided to
orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0.
Return the minimum number of edges changed.

It's guaranteed that each city can reach the city 0 after reorder.

Constraints:

2 <= n <= 5 * 10^4
connections.length == n-1
connections[i].length == 2
0 <= connections[i][0], connections[i][1] <= n-1
connections[i][0] != connections[i][1]
"""


class Solution:
    def minReorder(self, n, connections) -> int:
        res = 0
        remain_set = set(range(n - 1))
        target_set = {0}
        while target_set:
            new_remain_set = set()
            new_target_set = set()
            for index in remain_set:
                from_city, to_city = connections[index]
                if to_city in target_set:
                    new_target_set.add(from_city)
                elif from_city in target_set:
                    new_target_set.add(to_city)
                    res += 1
                else:
                    new_remain_set.add(index)

            remain_set = new_remain_set
            target_set = new_target_set

        return res

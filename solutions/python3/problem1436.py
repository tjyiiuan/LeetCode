# -*- coding: utf-8 -*-
"""
1436. Destination City

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to
cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore,
there will be exactly one destination city.

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.
"""


class Solution:
    def destCity(self, paths):
        in_city_set = set()
        out_city_set = set()
        for out_city, in_city in paths:
            in_city_set.add(in_city)
            out_city_set.add(out_city)

        return (in_city_set - out_city_set).pop()

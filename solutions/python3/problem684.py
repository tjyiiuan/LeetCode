# -*- coding: utf-8 -*-
"""
684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N),
with one additional edge added. The added edge has two different vertices chosen from 1 to N,
and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v,
that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes.
If there are multiple answers, return the answer that occurs last in the given 2D-array.
The answer edge [u, v] should be in the same format, with u < v.
"""


class Solution:
    def __init__(self):
        self.graph = {}

    def findRedundantConnection(self, edges):
        for node1, node2 in edges:
            if self._is_connected(node1, node2):
                return [node1, node2]
            else:
                self._add_edge(node1, node2)

    def _add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []

        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def _is_connected(self, node1, node2):
        if node1 not in self.graph:
            return False

        visited = set()
        search_queue = [node1]
        while search_queue:
            cur_node = search_queue.pop()

            visited.add(cur_node)
            for next_node in self.graph[cur_node]:
                if next_node not in visited and next_node not in search_queue:
                    search_queue.append(next_node)

        return node2 in visited

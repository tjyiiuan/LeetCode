# -*- coding: utf-8 -*-
"""
429. N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.res = []

    def levelOrder(self, root):
        self._traversal([root])
        return self.res

    def _traversal(self, node_list):
        res = []
        next_level = []
        for node in node_list:
            if not node:
                continue

            res.append(node.val)
            next_level.extend(node.children)

        if res:
            self.res.append(res)

        if next_level:
            self._traversal(next_level)

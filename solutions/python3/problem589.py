# -*- coding: utf-8 -*-
"""
589. N-ary Tree Preorder Traversal

Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Follow up:
Recursive solution is trivial, could you do it iteratively?


Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        res = []
        q = deque([root])
        while q:
            cur_node = q.popleft()
            if cur_node is None:
                continue
            res.append(cur_node.val)
            q.extendleft(cur_node.children[::-1])

        return res

# -*- coding: utf-8 -*-
"""
515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def largestValues(self, root):
        if root is not None:
            self._bfs([root])

        return self.res

    def _bfs(self, node_list):
        next_level = []
        val = -float("inf")

        for node in node_list:
            if node.val > val:
                val = node.val

            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)

        self.res.append(val)

        if next_level:
            self._bfs(next_level)

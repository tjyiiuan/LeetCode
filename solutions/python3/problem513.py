# -*- coding: utf-8 -*-
"""
513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Note: You may assume the tree (i.e., the given root node) is not NULL.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = None

    def findBottomLeftValue(self, root: TreeNode) -> int:
        self._bfs([root])

        return self.res

    def _bfs(self, node_list):
        next_level = []

        for node in node_list:
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)

        if next_level:
            self._bfs(next_level)
        else:
            self.res = node_list[0].val

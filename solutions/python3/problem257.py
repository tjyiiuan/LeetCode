# -*- coding: utf-8 -*-
"""
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.
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

    def binaryTreePaths(self, root):
        self._dfs(root, "")

        return self.res

    def _dfs(self, node, pre):
        if node is not None:
            path = "->".join((pre, str(node.val)))
            if node.left is None and node.right is None:
                self.res.append(path[2:])
            else:
                self._dfs(node.left, path)
                self._dfs(node.right, path)

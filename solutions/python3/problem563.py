# -*- coding: utf-8 -*-
"""
563. Binary Tree Tilt

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values
and the sum of all right subtree node values.
Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def findTilt(self, root: TreeNode) -> int:
        self._traverse(root)
        return self.res

    def _traverse(self, node):
        if node is None:
            return 0

        l_sum = self._traverse(node.left)
        r_sum = self._traverse(node.right)
        self.res += abs(l_sum - r_sum)

        return l_sum + r_sum + node.val

# -*- coding: utf-8 -*-
"""
530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values,
find the minimum absolute difference between values of any two nodes.

Note:
There are at least two nodes in this BST.
This question is the same as 783.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        value_list = self._traverse_bst(root)
        diff = value_list[1] - value_list[0]

        for ind, val in enumerate(value_list[2:], start=2):
            diff = min(val - value_list[ind - 1], diff)
        return diff

    def _traverse_bst(self, node):
        if node is None:
            return []

        return self._traverse_bst(node.left) + [node.val] + self._traverse_bst(node.right)

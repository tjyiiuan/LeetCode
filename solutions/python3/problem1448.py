# -*- coding: utf-8 -*-
"""
1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are
no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self._count_good_node(root)

    def _count_good_node(self, node, pre_max=-float("inf")):
        if node is None:
            return 0

        count = 0
        if node.val >= pre_max:
            count += 1
            pre_max = node.val

        return count + self._count_good_node(node.left, pre_max) + self._count_good_node(node.right, pre_max)

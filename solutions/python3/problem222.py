# -*- coding: utf-8 -*-
"""
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        l_depth = self._max_depth(root.left)
        r_depth = self._max_depth(root.right)

        if l_depth == r_depth:
            # left is complete
            return 2 ** l_depth + self.countNodes(root.right)
        else:
            # right is complete
            return 2 ** r_depth + self.countNodes(root.left)

    def _max_depth(self, node):
        if node is None:
            return 0

        return self._max_depth(node.left) + 1

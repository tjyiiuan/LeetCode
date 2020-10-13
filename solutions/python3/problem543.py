# -*- coding: utf-8 -*-
"""
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
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

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self._traverse(root)
        return self.res

    def _traverse(self, node):
        if node is None:
            return 0

        l_depth = self._traverse(node.left)
        r_depth = self._traverse(node.right)

        self.res = max(l_depth + r_depth, self.res)

        return max(l_depth, r_depth) + 1

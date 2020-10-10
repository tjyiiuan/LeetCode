# -*- coding: utf-8 -*-
"""
965. Univalued Binary Tree

A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Note:
The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root, val=None) -> bool:
        if root is None:
            return True

        return self._is_same_val(root, root.val)

    def _is_same_val(self, node, val):
        if node is None:
            return True

        return node.val == val and self._is_same_val(node.left, val) and self._is_same_val(node.right, val)

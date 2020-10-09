# -*- coding: utf-8 -*-
"""
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Follow up: Solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self._is_symmetric_node(root.left, root.right)
    def _is_symmetric_node(self, left, right):
        if left is None and right is None:
            return True
        elif left is not None and right is not None:
            if left.val != right.val:
                return False

            lsym = self._is_symmetric_node(left.left, right.right)
            rsym = self._is_symmetric_node(left.right, right.left)
            return lsym and rsym
        else:
            return False

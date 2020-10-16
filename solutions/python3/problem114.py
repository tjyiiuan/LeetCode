# -*- coding: utf-8 -*-
"""
114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self._flattern(root, None)

    def _flattern(self, node, right):
        if node is None:
            return right

        node.right = self._flattern(node.left, self._flattern(node.right, None))
        node.left = None

        cur_node = node
        while cur_node.right is not None:
            cur_node = cur_node.right

        cur_node.right = right

        return node

# -*- coding: utf-8 -*-
"""
783. Minimum Distance Between BST Nodes

Given a Binary Search Tree (BST) with the root node root,
return the minimum difference between the values of any two different nodes in the tree.

Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
This question is the same as 530.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        value_list = self._traverse_bst(root)
        diff = value_list[1] - value_list[0]

        for ind, val in enumerate(value_list[2:], start=2):
            diff = min(val - value_list[ind - 1], diff)
        return diff

    def _traverse_bst(self, node):
        if node is None:
            return []

        return self._traverse_bst(node.left) + [node.val] + self._traverse_bst(node.right)

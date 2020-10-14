# -*- coding: utf-8 -*-
"""
99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Follow up:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root.left is not None:
            l_max = self._max_node(root.left)
        else:
            l_max = None

        if root.right is not None:
            r_min = self._min_node(root.right)
        else:
            r_min = None

        self._swap_val(l_max, root, r_min)

        if root.left is not None:
            self.recoverTree(root.left)
        if root.right is not None:
            self.recoverTree(root.right)

    def _swap_val(self, *nodes):
        res = []
        for node in nodes:
            if node is not None:
                res.append(node)

        tmp = sorted((node.val for node in res))
        for ind, node in enumerate(res):
            node.val = tmp[ind]

    def _min_node(self, node):
        res = node

        if node.left is not None:
            tmp = self._min_node(node.left)
            if tmp.val < res.val:
                res = tmp

        if node.right is not None:
            tmp = self._min_node(node.right)
            if tmp.val < res.val:
                res = tmp

        return res

    def _max_node(self, node):
        res = node

        if node.left is not None:
            tmp = self._max_node(node.left)
            if tmp.val > res.val:
                res = tmp

        if node.right is not None:
            tmp = self._max_node(node.right)
            if tmp.val > res.val:
                res = tmp

        return res

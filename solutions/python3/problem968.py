# -*- coding: utf-8 -*-
"""
968. Binary Tree Cameras

Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root):
        _, res, _ = self._install_cam(root)
        return res

    def _install_cam(self, node):
        if node is None:
            return [float("inf"), 0, 0]

        la, lb, lc = self._install_cam(node.left)
        ra, rb, rc = self._install_cam(node.right)
        a = lc + rc + 1
        b = min(a, la + rb, ra + lb)
        c = min(a, lb + rb)
        return a, b, c

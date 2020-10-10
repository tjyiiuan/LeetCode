# -*- coding: utf-8 -*-
"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order,
the values of those leaves form a leaf value sequence.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self._get_leaf(root1) == self._get_leaf(root2)

    def _get_leaf(self, root):
        res = []

        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                continue

            if node.left is None and node.right is None:
                res.append(node.val)
            else:
                q.extendleft([node.left, node.right])

        return res

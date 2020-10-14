# -*- coding: utf-8 -*-
"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = True

    def isBalanced(self, root: TreeNode):
        self._traverse(root)
        return self.res

    def _traverse(self, node):
        if node is None:
            return 0

        l_depth = self._traverse(node.left)
        r_depth = self._traverse(node.right)

        if abs(l_depth - r_depth) > 1:
            self.res = False

        return max(l_depth, r_depth) + 1

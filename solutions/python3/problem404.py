# -*- coding: utf-8 -*-
"""
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.
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

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self._dfs(root, False)
        return self.res

    def _dfs(self, node, b_left):
        if node is None:
            return

        if node.left is None and node.right is None and b_left:
            # left leaf
            self.res += node.val
        else:
            self._dfs(node.left, True)
            self._dfs(node.right, False)

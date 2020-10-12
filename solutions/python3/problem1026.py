# -*- coding: utf-8 -*-
"""
1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B
where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
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

    def maxAncestorDiff(self, root) -> int:
        self._dfs(root, tuple())
        return self.res

    def _dfs(self, node, pre):
        if node is None:
            return
        for val in pre:
            self.res = max(self.res, abs(val - node.val))

        if not pre:
            pre = (node.val, )
        elif len(pre) == 1:
            if pre[0] > node.val:
                pre = (node.val, pre[0])
            else:
                pre = (pre[0], node.val)
        elif node.val > pre[1]:
            pre = (pre[0], node.val)
        elif node.val < pre[0]:
            pre = (node.val, pre[1])

        self._dfs(node.left, pre)
        self._dfs(node.right, pre)

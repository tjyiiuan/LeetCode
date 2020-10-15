# -*- coding: utf-8 -*-
"""
337. House Robber III

The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self._max_rob(root))

    def _max_rob(self, node):
        if node is None:
            return 0, 0
        elif node.left is None and node.right is None:
            return node.val, 0

        l_rob_t, l_lob_f = self._max_rob(node.left)
        r_rob_t, r_lob_f = self._max_rob(node.right)

        return l_lob_f + r_lob_f + node.val, max(l_rob_t, l_lob_f) + max(r_rob_t, r_lob_f)

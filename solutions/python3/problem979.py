# -*- coding: utf-8 -*-
"""
979. Distribute Coins in Binary Tree

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.



Note:

1<= N <= 100
0 <= node.val <= N
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

    def distributeCoins(self, root: TreeNode) -> int:
        self._dfs(root)
        return self.res

    def _dfs(self, node):
        if node is None:
            return 0

        l_val = self._dfs(node.left)
        r_val = self._dfs(node.right)
        self.res += abs(l_val) + abs(r_val)
        return node.val + l_val + r_val - 1

# -*- coding: utf-8 -*-
"""
865. Smallest Subtree with all the Deepest Nodes

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

Constraints:

The number of nodes in the tree will be in the range [1, 500].
The values of the nodes in the tree are unique.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = (1002, None, -1)

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        self._dfs(root)
        return self.res[1]

    def _dfs(self, node, parent_depth=0):
        cur_depth = parent_depth + 1
        if node.left is None:
            if node.right is None:
                # leaf
                self._add_res(cur_depth, node, cur_depth)
                return node, cur_depth
            else:
                return node, self._dfs(node.right, cur_depth)[1]
        else:
            if node.right is None:
                return node, self._dfs(node.left, cur_depth)[1]
            else:
                l_info = self._dfs(node.left, cur_depth)
                r_info = self._dfs(node.right, cur_depth)
                if l_info[1] == r_info[1]:
                    self._add_res(cur_depth, node, l_info[1])
                    return node, l_info[1]
                else:
                    return node, max(l_info[1], r_info[1])

    def _add_res(self, node_depth, node, deepest):
        if deepest > self.res[2]:
            self.res = (node_depth, node, deepest)
        elif deepest == self.res[2] and node_depth < self.res[0]:
            self.res = (node_depth, node, deepest)

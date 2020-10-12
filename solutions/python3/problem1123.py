# -*- coding: utf-8 -*-
"""
1123. Lowest Common Ancestor of Deepest Leaves

Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.

Constraints:
The given tree will have between 1 and 1000 nodes.
Each node of the tree will have a distinct value between 1 and 1000.
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

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
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

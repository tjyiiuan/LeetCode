# -*- coding: utf-8 -*-
"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
"The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself)."

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self._search(root, p.val, q.val)

    def _search(self, node, p, q):
        if node is None:
            return None
        elif node.val == p or node.val == q:
            return node

        l_res = self._search(node.left, p, q)
        r_res = self._search(node.right, p, q)

        if l_res is None:
            if r_res is None:
                return None
            else:
                return r_res
        elif r_res is None:
            return l_res
        else:
            return node

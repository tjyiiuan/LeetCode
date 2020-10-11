# -*- coding: utf-8 -*-
"""
606. Construct String from Binary Tree

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder
traversing way.

The null node needs to be represented by empty parenthesis pair "()".
And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between
the string and the original binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""

        res = str(t.val)
        if t.right is not None:
            res += self.tree2str(t.left).join(["(", ")"])
            res += self.tree2str(t.right).join(["(", ")"])
        elif t.left is not None:
            res += self.tree2str(t.left).join(["(", ")"])

        return res

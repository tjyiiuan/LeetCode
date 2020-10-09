# -*- coding: utf-8 -*-
"""
617. Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Note: The merging process must start from the root nodes of both trees.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        elif t2 is None:
            return t1

        val = t1.val + t2.val
        lnode = self.mergeTrees(t1.left, t2.left)
        rnode = self.mergeTrees(t1.right, t2.right)

        return TreeNode(val=val, left=lnode, right=rnode)

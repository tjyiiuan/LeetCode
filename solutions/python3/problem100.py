# -*- coding: utf-8 -*-
"""
100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif q == None and p != None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


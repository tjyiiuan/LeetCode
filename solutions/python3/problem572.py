# -*- coding: utf-8 -*-
"""
572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values
with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        q = Queue()
        q.put(s)
        while not q.empty():
            node = q.get()
            if self._is_same(node, t):
                return True

            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

        return False

    def _is_same(self, s_node, t):
        if s_node is None:
            if t is None:
                return True
            else:
                return False
        elif t is None:
            return False
        else:
            if s_node.val != t.val:
                return False

            return self._is_same(s_node.left, t.left) and self._is_same(s_node.right, t.right)

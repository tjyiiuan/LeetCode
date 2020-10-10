# -*- coding: utf-8 -*-
"""
226. Invert Binary Tree

Invert a binary tree.

Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew),
but you can’t invert a binary tree on a whiteboard so f*** off.
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if node is None:
                continue

            node.left, node.right = node.right, node.left
            q.put(node.left)
            q.put(node.right)

        return root

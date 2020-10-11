# -*- coding: utf-8 -*-
"""
107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        q = Queue()
        q.put([root])
        res = []

        while not q.empty():
            this_val_list = []
            this_node_list = []

            node_list = q.get()
            for node in node_list:
                if node is None:
                    continue
                this_val_list.append(node.val)
                this_node_list.append(node.left)
                this_node_list.append(node.right)

            if this_val_list:
                res.append(this_val_list)

            if this_node_list:
                q.put(this_node_list)

        return res[::-1]

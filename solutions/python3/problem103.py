# -*- coding: utf-8 -*-
"""
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        node_list = [root]
        order = -1
        while node_list:
            order = - order
            this_val_list = []
            next_node_list = []
            for node in node_list:
                if node is None:
                    continue

                this_val_list.append(node.val)
                next_node_list.append(node.left)
                next_node_list.append(node.right)

            node_list = next_node_list
            if this_val_list:
                res.append(this_val_list[::order])

        return res

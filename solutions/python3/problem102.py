# -*- coding: utf-8 -*-
"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        res = []
        node_list = [root]
        while node_list:
            this_val = []
            next_list = []
            for node in node_list:
                if node is None:
                    continue
                this_val.append(node.val)
                next_list.append(node.left)
                next_list.append(node.right)

            if this_val:
                res.append(this_val)

            node_list = next_list

        return res

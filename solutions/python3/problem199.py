# -*- coding: utf-8 -*-
"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        res = []
        node_list = [root]

        while node_list:
            pre = None
            next_node_list = []
            for node in node_list:
                if node is None:
                    continue

                if pre is None:
                    pre = node
                    res.append(node.val)

                next_node_list.append(node.right)
                next_node_list.append(node.left)
            node_list = next_node_list

        return res

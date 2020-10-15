# -*- coding: utf-8 -*-
"""
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target_sum):
        res = []
        stack = [(0, (), root)]
        while stack:
            cur_sum, path, node = stack.pop()
            if node is None:
                continue

            cur_sum += node.val
            path += (node.val,)

            if node.left is None and node.right is None:
                # leaf
                if cur_sum == target_sum:
                    res.append(list(path))
            else:
                stack.append((cur_sum, path, node.left))
                stack.append((cur_sum, path, node.right))

        return res

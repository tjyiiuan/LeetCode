# -*- coding: utf-8 -*-
"""
637. Average of Levels in Binary Tree

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Note:
The range of node's value is in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        cur_level = [root]
        while cur_level:
            cur_value = []
            next_level = []
            for node in cur_level:
                cur_value.append(node.val)

                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            if cur_value:
                res.append(sum(cur_value) / len(cur_value))
            cur_level = next_level

        return res

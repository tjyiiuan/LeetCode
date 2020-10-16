# -*- coding: utf-8 -*-
"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        stack = [(0, root)]
        while stack:
            pre, node = stack.pop()
            if node is None:
                continue

            pre = pre * 10 + node.val

            if node.left is None and node.right is None:
                res += pre
            else:
                stack.append((pre, node.left))
                stack.append((pre, node.right))

        return res

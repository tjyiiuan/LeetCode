# -*- coding: utf-8 -*-
"""
501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element)
in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space?
(Assume that the implicit stack space incurred due to recursion does not count).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = {}

    def findMode(self, root):
        self._traverse(root)

        res = []
        max_count = 0
        for val, count in self.res.items():
            if count > max_count:
                res = [val]
                max_count = count
            elif count == max_count:
                res.append(val)

        return res

    def _traverse(self, node):
        if not node:
            return

        if node.val not in self.res:
            self.res[node.val] = 1
        else:
            self.res[node.val] += 1

        self._traverse(node.left)
        self._traverse(node.right)

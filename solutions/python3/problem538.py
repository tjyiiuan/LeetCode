# -*- coding: utf-8 -*-
"""
538. Convert BST to Greater Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST
is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Note: This question is the same as 1038

Constraints:
The number of nodes in the tree is in the range [0, 104].
-104 <= Node.val <= 104
All the values in the tree are unique.
root is guaranteed to be a valid binary search tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root):
        cur_sum = 0
        node_list = self._traverse(root)
        for node in node_list[::-1]:
            node.val += cur_sum
            cur_sum = node.val

        return root

    def _traverse(self, node):
        if node is None:
            return []

        return self._traverse(node.left) + [node] + self._traverse(node.right)

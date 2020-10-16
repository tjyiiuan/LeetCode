# -*- coding: utf-8 -*-
"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        length = len(preorder)
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(val=preorder[0])
        else:
            root_val = preorder[0]

            in_ind = inorder.index(root_val)
            l_in = inorder[0:in_ind]
            r_in = inorder[in_ind + 1:]

            l_pre = preorder[1:len(l_in) + 1]
            r_pre = preorder[len(l_in) + 1:]

            l_node = self.buildTree(l_pre, l_in)
            r_node = self.buildTree(r_pre, r_in)

            return TreeNode(val=root_val, left=l_node, right=r_node)

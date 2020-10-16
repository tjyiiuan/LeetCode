# -*- coding: utf-8 -*-
"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

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
    def buildTree(self, inorder, postorder):
        length = len(postorder)
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(val=postorder[0])
        else:
            root_val = postorder[-1]

            in_ind = inorder.index(root_val)
            l_in = inorder[0:in_ind]
            r_in = inorder[in_ind + 1:]

            l_post = postorder[:len(l_in)]
            r_post = postorder[len(l_in):-1]

            l_node = self.buildTree(l_in, l_post)
            r_node = self.buildTree(r_in, r_post)

            return TreeNode(val=root_val, left=l_node, right=r_node)

# -*- coding: utf-8 -*-
"""
1008. Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has
a value < node.val, and any descendant of node.right has a value > node.val.
Also recall that a preorder traversal displays the value of the node first, then traverses node.left,
then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree
with the given requirements.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        if not preorder:
            return None

        root_val = preorder[0]
        ind = 1
        length = len(preorder) - 1
        while ind <= length:
            if preorder[ind] > root_val:
                break
            ind += 1

        l_node = self.bstFromPreorder(preorder[1:ind])
        r_node = self.bstFromPreorder(preorder[ind:])

        return TreeNode(val=root_val, left=l_node, right=r_node)

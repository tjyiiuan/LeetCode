# -*- coding: utf-8 -*-
"""
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        res, _, _ = self._validate(root)
        return res

    def _validate(self, node):
        if node.left:
            l_res, l_max, l_min = self._validate(node.left)
            if not l_res:
                return False, 0, 0
            if node.right:
                r_res, r_max, r_min = self._validate(node.right)
                if not r_res:
                    return False, 0, 0
                elif not l_max < node.val < r_min:
                    return False, 0, 0
                else:
                    return True, r_max, l_min
            else:
                if not l_max < node.val:
                    return False, 0, 0
                else:
                    return True, node.val, l_min
        elif node.right:
            r_res, r_max, r_min = self._validate(node.right)
            if not r_res:
                return False, 0, 0
            elif not node.val < r_min:
                return False, 0, 0
            else:
                return True, r_max, node.val
        else:
            return True, node.val, node.val,

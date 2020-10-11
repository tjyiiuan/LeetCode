# -*- coding: utf-8 -*-
"""
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        else:
            re_sum = sum - root.val
            if root.left is None and root.right is None:
                # leaf node
                if re_sum != 0:
                    return False
                return True
            elif root.left is None and root.right is not None:
                return self.hasPathSum(root.right, re_sum)
            elif root.left is not None and root.right is None:
                return self.hasPathSum(root.left, re_sum)
            else:
                return self.hasPathSum(root.left, re_sum) or self.hasPathSum(root.right, re_sum)

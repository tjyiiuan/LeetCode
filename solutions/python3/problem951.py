# -*- coding: utf-8 -*-
"""
951. Flip Equivalent Binary Trees

For a binary tree T, we can define a flip operation as follows:
choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y
after some number of flip operations.

Given the roots of two binary trees root1 and root2,
return true if the two trees are flip equivelent or false otherwise.

Constraints:
The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            if root1.val != root2.val:
                return False
            if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right):
                return True
            else:
                return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        else:
            return False

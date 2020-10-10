# -*- coding: utf-8 -*-
"""
897. Increasing Order Search Tree

Given a binary search tree,
rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree,
and every node has no left child and only 1 right child.

Constraints:
The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root, parent=None) -> TreeNode:
        if root is None:
            return None
        else:
            if root.right is None:
                root.right = parent
            else:
                root.right = self.increasingBST(root.right, parent=parent)

            if root.left is None:
                return root
            else:
                left_node = self.increasingBST(root.left, parent=root)
                root.left = None
                return left_node

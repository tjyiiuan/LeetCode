# -*- coding: utf-8 -*-
"""
144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up:
Recursive solution is trivial, could you do it iteratively?
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal_(self, root: TreeNode):
        # recursive
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal(self, root):
        # iterative
        res = []
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node is None:
                continue

            res.append(node.val)
            dq.extendleft([node.right, node.left])

        return res

# -*- coding: utf-8 -*-
"""
145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Constraints:
The number of the nodes in the tree is in the range [0, 100].
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
    def postorderTraversal_(self, root: TreeNode):
        # recursive
        if root is None:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal(self, root: TreeNode):
        # iterative

        res = []
        stack = [root]
        pre = None
        while stack:
            node = stack[-1]
            if node is None:
                stack.pop()
                continue

            if node.left is None and node.right is None:
                res.append(node.val)
                stack.pop()
                pre = node
            elif pre is not None and (pre is node.left or pre is node.right):
                res.append(node.val)
                stack.pop()
                pre = node
            else:
                stack.append(node.right)
                stack.append(node.left)

        return res

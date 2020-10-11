# -*- coding: utf-8 -*-
"""
653. Two Sum IV - Input is a BST

Given the root of a Binary Search Tree and a target number k,
return true if there exist two elements in the BST such that their sum is equal to the given target.
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        value_set = set()
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if node is None:
                continue

            if k - node.val in value_set:
                return True

            value_set.add(node.val)
            q.put(node.left)
            q.put(node.right)

        return False

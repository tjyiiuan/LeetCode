# -*- coding: utf-8 -*-
"""
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer
must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        orig_q = Queue()
        orig_q.put(original)
        clon_q = Queue()
        clon_q.put(cloned)

        while not orig_q.empty():
            orig_node = orig_q.get()
            clon_node = clon_q.get()

            if orig_node is None:
                continue
            elif orig_node is target:
                return clon_node
            else:
                orig_q.put(orig_node.left)
                orig_q.put(orig_node.right)
                clon_q.put(clon_node.left)
                clon_q.put(clon_node.right)

        return None

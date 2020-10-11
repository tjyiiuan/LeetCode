# -*- coding: utf-8 -*-
"""
1315. Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        value_list = []
        q = Queue()
        q.put((False, root))
        while not q.empty():
            b_valid_parent, node = q.get()
            if node is None:
                continue
            elif b_valid_parent:
                if node.left is not None:
                    value_list.append(node.left.val)

                if node.right is not None:
                    value_list.append(node.right.val)

            b_valid = node.val % 2 == 0
            q.put((b_valid, node.left))
            q.put((b_valid, node.right))

        if not value_list:
            return 0

        return sum(value_list)

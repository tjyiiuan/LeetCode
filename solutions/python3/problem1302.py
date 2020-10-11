# -*- coding: utf-8 -*-
"""
1302. Deepest Leaves Sum

Given a binary tree, return the sum of values of its deepest leaves.


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
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = Queue()
        q.put((0, root))
        value_list = []
        deep = -1

        while not q.empty():
            depth, node = q.get()
            if node is None:
                continue
            elif node.left is None and node.right is None:
                # leaf
                if depth > deep:
                    deep = depth
                    value_list = [node.val]
                elif depth == deep:
                    value_list.append(node.val)
            else:
                q.put((depth + 1, node.left))
                q.put((depth + 1, node.right))

        if not value_list:
            return 0
        else:
            return sum(value_list)

# -*- coding: utf-8 -*-
"""
671. Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value,
where each node in this tree has exactly two or zero sub-node.
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes'
value in the whole tree.

If no such second minimum value exists, output -1 instead.
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        value_set = set()
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if node is None:
                continue
            value_set.add(node.val)
            q.put(node.left)
            q.put(node.right)

        min_val, res_val = root.val, float('inf')
        for val in value_set:
            if min_val < val < res_val:
                res_val = val

        if res_val < float('inf'):
            return res_val

        return -1

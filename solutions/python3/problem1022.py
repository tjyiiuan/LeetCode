# -*- coding: utf-8 -*-
"""
1022. Sum of Root To Leaf Binary Numbers

You are given the root of a binary tree where each node has a value 0 or 1.
Each root-to-leaf path represents a binary number starting with the most significant bit.
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = Queue()
        q.put([0, root])
        res = 0
        while not q.empty():
            pre, node = q.get()
            pre = 2 * pre + node.val

            if node.left is None and node.right is None:
                res += pre
            else:
                if node.left is not None:
                    q.put([pre, node.left])

                if node.right is not None:
                    q.put([pre, node.right])

        return res

# -*- coding: utf-8 -*-
"""
2265. Count Nodes Equal to Average of Subtree

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the
values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self._count = 0

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self._check_node(root)
        return self._count

    def _check_node(self, node: Optional[TreeNode]) -> (int, int):
        if not node:
            return (0, 0)

        l_sum, l_count = self._check_node(node.left)
        r_sum, r_count = self._check_node(node.right)
        t_sum = l_sum + r_sum + node.val
        t_count = l_count + r_count + 1
        if t_sum // t_count == node.val:
            self._count += 1

        return (t_sum, t_count)

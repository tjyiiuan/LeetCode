# -*- coding: utf-8 -*-
"""
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_lvl = -1
        max_val = -float("inf")

        q = Queue()
        q.put((1, [root]))
        while not q.empty():
            level, node_list = q.get()
            next_node_list = []
            cur_val = 0

            for node in node_list:
                cur_val += node.val

                if node.left is not None:
                    next_node_list.append(node.left)

                if node.right is not None:
                    next_node_list.append(node.right)

            if next_node_list:
                q.put((level + 1, next_node_list))

            if cur_val > max_val:
                max_lvl = level
                max_val = cur_val

        return max_lvl

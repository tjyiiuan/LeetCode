# -*- coding: utf-8 -*-
"""
1372. Longest ZigZag Path in a Binary Tree

Given a binary tree root, a ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right then move to the right child of the current node otherwise move to the left child.
Change the direction from right to left or right to left.
Repeat the second and third step until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Constraints:

Each tree has at most 50000 nodes..
Each node's value is between [1, 100].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def longestZigZag(self, root: TreeNode) -> int:
        self._traverse(root, -1)
        return self.res

    def _traverse(self, node, node_visited, b_left=True):
        if node is None:
            self.res = max(self.res, node_visited)
            return

        node_visited += 1

        if node_visited == 0:
            self._traverse(node.left, node_visited, True)
            self._traverse(node.right, node_visited, False)
        else:
            if b_left:
                self._traverse(node.left, 0, True)
                self._traverse(node.right, node_visited, False)
            else:
                self._traverse(node.left, node_visited, True)
                self._traverse(node.right, 0, False)

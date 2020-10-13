# -*- coding: utf-8 -*-
"""
1305. All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1, root2):
        node_val1 = self._traverse_bst(root1)
        node_val2 = self._traverse_bst(root2)

        res = []
        ind1 = 0
        ind2 = 0
        length1 = len(node_val1) - 1
        length2 = len(node_val2) - 1

        while ind1 <= length1 and ind2 <= length2:
            if node_val1[ind1] <= node_val2[ind2]:
                res.append(node_val1[ind1])
                ind1 += 1
            else:
                res.append(node_val2[ind2])
                ind2 += 1

        res += node_val1[ind1:]
        res += node_val2[ind2:]

        return res

    def _traverse_bst(self, node):
        if node is None:
            return []

        return self._traverse_bst(node.left) + [node.val] + self._traverse_bst(node.right)

# -*- coding: utf-8 -*-
"""
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        return self._search(root, k)[k - 1]

    def _search(self, node, k):
        if node is None:
            return []

        left_res = self._search(node.left, k)
        remain = k - len(left_res)
        if remain <= 0:
            return left_res
        elif remain == 1:
            return left_res + [node.val]
        else:
            return left_res + [node.val] + self._search(node.right, remain)

# -*- coding: utf-8 -*-
"""
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        length = len(nums)
        if length == 0:
            return None

        mid_ind = length // 2
        l_tree = self.sortedArrayToBST(nums[:mid_ind])
        r_tree = self.sortedArrayToBST(nums[mid_ind + 1:])
        root = TreeNode(val=nums[mid_ind], left=l_tree, right=r_tree)

        return root

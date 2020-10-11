# -*- coding: utf-8 -*-
"""
654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if not nums:
            return None

        max_val = nums[0]
        max_ind = 0
        for ind, val in enumerate(nums):
            if val > max_val:
                max_ind = ind
                max_val = val

        l_node = self.constructMaximumBinaryTree(nums[:max_ind])
        r_node = self.constructMaximumBinaryTree(nums[max_ind + 1:])
        root = TreeNode(val=max_val, left=l_node, right=r_node)

        return root

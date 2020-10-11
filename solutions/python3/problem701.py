# -*- coding: utf-8 -*-
"""
701. Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion. It is guaranteed that the new value
does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if root is None:
            return node

        cur_node = root
        while True:
            if cur_node.val < val:
                if cur_node.right is None:
                    cur_node.right = node
                    return root
                else:
                    cur_node = cur_node.right
            else:
                if cur_node.left is None:
                    cur_node.left = node
                    return root
                else:
                    cur_node = cur_node.left

        return None

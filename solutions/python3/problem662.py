# -*- coding: utf-8 -*-
"""
662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes
(the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also
counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        level = 0
        node_list = [(1, root)]
        while node_list:
            next_node_list = []
            first_index = None
            last_index = None
            level += 1
            for node_index, node in node_list:
                if node is None:
                    continue

                if first_index is None:
                    first_index = node_index
                    last_index = node_index
                else:
                    last_index = node_index

                left_index = 2 * node_index - 1
                next_node_list.append((left_index, node.left))
                next_node_list.append((left_index + 1, node.right))

            node_list = next_node_list

            if first_index is not None:
                res = max(res, last_index - first_index + 1)

        return res

# -*- coding: utf-8 -*-
"""
655. Print Binary Tree

Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.

The column number n should always be an odd number.

The root node's value (in string format) should be put in the exactly middle of the first row it can be put.
The column and the row where the root node belongs will separate the rest space into two parts
(left-bottom part and right-bottom part).
You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part.
The left-bottom part and the right-bottom part should have the same size.
Even if one subtree is none while the other is not, you don't need to print anything for the none subtree
but still need to leave the space as large as that for the other subtree. However, if two subtrees are none,
then you don't need to leave space for both of them.

Each unused space should contain an empty string "".

Print the subtrees following the same rules.

Note: The height of binary tree is in the range of [1, 10].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root):
        value_list = []
        node_list = [[1, root]]
        max_level = -1

        while node_list:
            max_level += 1
            this_val_list = []
            next_node_list = []

            for ind, node in node_list:
                if node is None:
                    continue
                this_val_list.append((ind, node.val))

                next_node_list.append((2 * ind - 1, node.left))
                next_node_list.append((2 * ind, node.right))

            node_list = next_node_list

            if this_val_list:
                value_list.append(this_val_list)

        length = 2 ** max_level - 1
        prefix = length
        res = []
        for level_ind, node_list in enumerate(value_list):
            this_level = [""] * length
            prefix = prefix // 2
            for node_ind, node_val in node_list:
                this_level[(2 * node_ind - 1) * prefix + 2 * node_ind - 2] = str(node_val)
            res.append(this_level)

        return res

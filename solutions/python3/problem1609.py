# -*- coding: utf-8 -*-
"""
1609. Even Odd Tree

A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1,
their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order
(from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order
(from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 106
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        node_list = [root]
        node_level = -1
        sign = -1

        while node_list:
            node_level += 1
            next_node_list = []
            pre_val = None
            sign = -sign

            for node in node_list:
                if node is None:
                    continue

                if not (node.val + node_level) % 2 == 1:
                    return False

                if pre_val is not None and (node.val - pre_val) * sign <= 0:
                    return False

                pre_val = node.val

                next_node_list.append(node.left)
                next_node_list.append(node.right)

            node_list = next_node_list

        return True

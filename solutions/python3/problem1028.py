# -*- coding: utf-8 -*-
"""
1028. Recover a Tree From Preorder Traversal

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node),
then we output the value of this node.
(If the depth of a node is D, the depth of its immediate child is D+1. The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

Note:
The number of nodes in the original tree is between 1 and 1000.
Each node will have a value between 1 and 10^9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        value_list = []
        cur_level = 0
        last_char = ""
        last_val = ""

        for char in S:
            if char == "-":
                if last_char != "-":
                    value_list.append([cur_level, int(last_val)])
                    last_val = ""
                    cur_level = 0
                cur_level += 1
            else:
                last_val += char

            last_char = char

        value_list.append([cur_level, int(last_val)])

        return self._construct(value_list)

    def _construct(self, value_list):
        if not value_list:
            return None

        length = len(value_list) - 1
        if length == 0:
            return TreeNode(val=value_list[0][1])

        next_level = value_list[1][0]
        ind = 2

        while ind <= length:
            lvl, _ = value_list[ind]
            if lvl == next_level:
                break
            ind += 1

        l_node = self._construct(value_list[1: ind])
        r_node = self._construct(value_list[ind:])

        return TreeNode(val=value_list[0][1], left=l_node, right=r_node)

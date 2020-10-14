# -*- coding: utf-8 -*-
"""
958. Check Completeness of a Binary Tree

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Note:
The tree will have between 1 and 100 nodes.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root):
        node_list = [root]
        pre_lvl_full = True

        while node_list:
            next_node_list = []
            first_node = node_list[0]
            if first_node is None:
                for node in node_list[1:]:
                    if node is not None:
                        return False
            else:
                next_node_list.append(first_node.left)
                next_node_list.append(first_node.right)
                if not pre_lvl_full:
                    return False
                pre_lvl_full = True
                for ind, node in enumerate(node_list[1:], start=1):
                    if node is not None:
                        if node_list[ind - 1] is None:
                            return False
                        else:
                            next_node_list.append(node.left)
                            next_node_list.append(node.right)
                    else:
                        pre_lvl_full = False

            node_list = next_node_list

        return True

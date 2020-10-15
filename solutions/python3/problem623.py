# -*- coding: utf-8 -*-
"""
623. Add One Row to Tree

Given the root of a binary tree, then value v and depth d,
you need to add a row of nodes with value v at the given depth d.
The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1,
create two tree nodes with value v as N's left subtree root and right subtree root.
And N's original left subtree should be the left subtree of the new left subtree root,
its original right subtree should be the right subtree of the new right subtree root.
If depth d is 1 that means there is no depth d-1 at all,
then create a tree node with value v as the new root of the whole original tree,
and the original tree is the new root's left subtree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(val=v, left=root)

        target_depth = d - 1
        cur_depth = 0
        node_list = [root]
        while node_list:
            next_node_list = []
            cur_depth += 1
            if cur_depth == target_depth:
                for node in node_list:
                    if node is None:
                        continue
                    node.left = TreeNode(val=v, left=node.left)
                    node.right = TreeNode(val=v, right=node.right)

                return root
            else:
                for node in node_list:
                    if node is None:
                        continue

                    next_node_list.append(node.left)
                    next_node_list.append(node.right)

                node_list = next_node_list

        return root

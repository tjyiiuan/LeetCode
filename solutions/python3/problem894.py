# -*- coding: utf-8 -*-
"""
894. All Possible Full Binary Trees

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.
Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.


Note:
1 <= N <= 20
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, N: int):
        if N == 1:
            return [TreeNode()]
        elif N % 2 == 0:
            return []

        res = []
        l_node_count = 1
        r_node_count = N - 2
        while True:
            if r_node_count < l_node_count:
                break
            if r_node_count > l_node_count:
                for one_l_node in self.allPossibleFBT(l_node_count):
                    for one_r_node in self.allPossibleFBT(r_node_count):
                        res.append(TreeNode(left=one_l_node, right=one_r_node))
                        res.append(TreeNode(left=one_r_node, right=one_l_node))
            else:
                tmp = self.allPossibleFBT(l_node_count)
                for one_l_node in tmp:
                    for one_r_node in tmp:
                        res.append(TreeNode(left=one_l_node, right=one_r_node))

            l_node_count += 2
            r_node_count -= 2

        return res

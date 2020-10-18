# -*- coding: utf-8 -*-
"""
971. Flip Binary Tree To Match Preorder Traversal

Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.
Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value,
then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches
the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.
You may return the answer in any order.

If we cannot do so, then return the list [-1].

Note:

1 <= N <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage):
        return list(self._dfs(root, voyage))

    def _dfs(self, node, voyage):
        if node is None:
            return ()

        if not voyage:
            return (-1,)

        if node.val != voyage[0]:
            return (-1,)

        if node.left is None:
            return self._dfs(node.right, voyage[1:])
        elif node.right is None:
            return self._dfs(node.left, voyage[1:])
        else:
            if node.left.val not in voyage:
                return (-1,)
            l_ind = voyage.index(node.left.val)

            if node.right.val not in voyage:
                return (-1,)
            r_ind = voyage.index(node.right.val)

            if l_ind > r_ind:
                tmp = (node.val,)

                l_res = self._dfs(node.left, voyage[l_ind:])
                r_res = self._dfs(node.right, voyage[1:l_ind])

            else:
                tmp = ()
                l_res = self._dfs(node.right, voyage[r_ind:])
                r_res = self._dfs(node.left, voyage[1:r_ind])

            if l_res == (-1,) or r_res == (-1,):
                return (-1, )
            else:
                return tmp + l_res + r_res

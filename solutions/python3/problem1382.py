# -*- coding: utf-8 -*-
"""
1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values.
If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self._bst(self._get_all_node(root))

    def _get_all_node(self, node):
        if not node:
            return []

        return self._get_all_node(node.left) + [node] + self._get_all_node(node.right)

    def _bst(self, nodes):
        if not nodes:
            return None

        count = len(nodes)
        root_index = count // 2
        root = nodes[root_index]
        root.left = self._bst(nodes[:root_index])
        root.right = self._bst(nodes[root_index + 1:])

        return root

# -*- coding: utf-8 -*-
"""
988. Smallest String Starting From Leaf

Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z':
a value of 0 represents 'a', a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller:
for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        return min(self._allstring(root))

    def _allstring(self, node):
        char = chr(node.val + 97)
        if node.left is None:
            if node.right is None:
                res = ("", )
            else:
                res = self._allstring(node.right)
        elif node.right is None:
            res = self._allstring(node.left)
        else:
            res = tuple(self._allstring(node.left) + self._allstring(node.right))

        return tuple(one_string + char for one_string in res)

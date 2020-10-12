# -*- coding: utf-8 -*-
"""
1457. Pseudo-Palindromic Paths in a Binary Tree

Given a binary tree where node values are digits from 1 to 9.
A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values
in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Constraints:
The given binary tree will have between 1 and 10^5 nodes.
Node values are digits from 1 to 9.
"""
from queue import Queue
import copy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        res = 0

        q = Queue()
        q.put((set(), root))
        while not q.empty():
            pre_set, node = q.get()

            if node.val in pre_set:
                pre_set.remove(node.val)
            else:
                pre_set.add(node.val)

            if node.left is None and node.right is None:
                # leaf node

                if len(pre_set) <= 1:
                    res += 1
            else:
                if node.left is not None:
                    q.put((copy.copy(pre_set), node.left))
                if node.right is not None:
                    q.put((copy.copy(pre_set), node.right))

        return res

# -*- coding: utf-8 -*-
"""
1469. Find All The Lonely Nodes

In a binary tree, a lonely node is a node that is the only child of its parent node.
The root of the tree is not lonely because it does not have a parent node.

Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree.
Return the list in any order.

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Each node's value is between [1, 10^6].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: TreeNode):
        res = []
        if not root:
            return res

        if not root.left:
            if not root.right:
                return res
            else:
                res.append(root.right.val)
                res.extend(self.getLonelyNodes(root.right))
        else:
            res.extend(self.getLonelyNodes(root.left))
            if not root.right:
                res.append(root.left.val)
            else:
                res.extend(self.getLonelyNodes(root.right))

        return res

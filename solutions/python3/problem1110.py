# -*- coding: utf-8 -*-
"""
1110. Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

Constraints:
The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []
        self.to_delete = None

    def delNodes(self, root: TreeNode, to_delete):
        self.to_delete = set(to_delete)
        self._del_node(True, root)
        return self.res

    def _del_node(self, del_parent, root):
        if root is None:
            return None

        if root.val in self.to_delete:
            self._del_node(True, root.left)
            self._del_node(True, root.right)
            return None
        else:
            root.left = self._del_node(False, root.left)
            root.right = self._del_node(False, root.right)
            if del_parent:
                self.res.append(root)
            return root

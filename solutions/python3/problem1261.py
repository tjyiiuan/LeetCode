# -*- coding: utf-8 -*-
"""
1261. Find Elements in a Contaminated Binary Tree

Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

You need to first recover the binary tree and then implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contamined binary tree, you need to recover it first.
bool find(int target) Return if the target value exists in the recovered binary tree.

Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 10^4]
Total calls of find() is between [1, 10^4]
0 <= target <= 10^6
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
class FindElements:
    def __init__(self, root: TreeNode):
        self.cache = set()
        root.val = 0

        # recover
        q = Queue()
        q.put(root)
        count = 0
        while not q.empty():
            node = q.get()
            self.cache.add(node.val)

            if node.left is not None:
                node.left.val = node.val * 2 + 1
                q.put(node.left)

            if node.right is not None:
                node.right.val = node.val * 2 + 2
                q.put(node.right)

    def find(self, target: int) -> bool:
        return target in self.cache

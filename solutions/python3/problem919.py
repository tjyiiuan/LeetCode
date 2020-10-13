# -*- coding: utf-8 -*-
"""
919. Complete Binary Tree Inserter

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled,
and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree
and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains
complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
"""

from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.cur_node = None
        self.node_q = Queue()
        self.node_q.put(root)
        while True:
            cur_node = self.node_q.get()
            if cur_node.left is None:
                self.cur_node = cur_node
                break
            else:
                self.node_q.put(cur_node.left)

            if cur_node.right is None:
                self.cur_node = cur_node
                break
            else:
                self.node_q.put(cur_node.right)

    def insert(self, v: int):
        node = TreeNode(val=v)
        self.node_q.put(node)

        if self.cur_node.left is None:
            self.cur_node.left = node
            return self.cur_node.val
        else:
            self.cur_node.right = node
            cur_node = self.cur_node
            self.cur_node = self.node_q.get()
            return cur_node.val

    def get_root(self) -> TreeNode:
        return self.root

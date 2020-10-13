# -*- coding: utf-8 -*-
"""
993. Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Constraints:
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int):
        res = {}

        q = Queue()
        q.put([(root, None)])
        level = 0
        while not q.empty():
            level += 1
            node_list = q.get()
            next_node_list = []
            for node, parent in node_list:
                if node.val == x:
                    res[x] = [level, parent]
                    if y in res:
                        return res[x][0] == res[y][0] and res[x][1] != res[y][1]
                elif node.val == y:
                    res[y] = [level, parent]
                    if x in res:
                        return res[x][0] == res[y][0] and res[x][1] != res[y][1]

                if node.left:
                    next_node_list.append((node.left, node.val))
                if node.right:
                    next_node_list.append((node.right, node.val))

            if next_node_list:
                q.put(next_node_list)

        return res[x][0] == res[y][0] and res[x][1] != res[y][1]

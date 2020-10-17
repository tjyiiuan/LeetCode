# -*- coding: utf-8 -*-
"""
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        self._connect(root)
        return root

    def _connect(self, node):
        if node.left is None:
            return (node,), (node,)

        l_l, l_r = self._connect(node.left)
        r_l, r_r = self._connect(node.right)
        for l_node, r_node in zip(l_r, r_l):
            l_node.next = r_node

        return l_l + (node,), r_r + (node,)


class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        left_most = root
        while left_most.left is not None:
            cur_node = left_most
            while cur_node is not None:
                cur_node.left.next = cur_node.right
                if cur_node.next:
                    cur_node.right.next = cur_node.next.left

                cur_node = cur_node.next

            left_most = left_most.left

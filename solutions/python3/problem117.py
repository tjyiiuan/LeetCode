# -*- coding: utf-8 -*-
"""
117. Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Constraints:
The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        left_most = root
        while left_most is not None:
            this_lvl_node = left_most
            cur_node, this_lvl_node, b = self._find_next_node(this_lvl_node, False)
            next_left_most = cur_node

            while cur_node is not None:
                next_node, this_lvl_node, b = self._find_next_node(this_lvl_node, b)
                cur_node.next = next_node
                cur_node = cur_node.next

            left_most = next_left_most

        return root

    def _find_next_node(self, node, b_left):
        if node is None:
            return None, None, False

        if b_left:
            if node.right is not None:
                return node.right, node.next, False
            else:
                return self._find_next_node(node.next, False)
        else:
            if node.left is not None:
                return node.left, node, True
            else:
                return self._find_next_node(node, True)

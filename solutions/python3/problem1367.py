# -*- coding: utf-8 -*-
"""
1367. Linked List in Binary Tree

Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head correspond to
some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

Constraints:

1 <= node.val <= 100 for each node in the linked list and binary tree.
The given linked list will contain between 1 and 100 nodes.
The given binary tree will contain between 1 and 2500 nodes.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head is None:
            return True

        if root is None:
            return False

        return self._dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def _dfs(self, head, root):
        if head is None:
            return True

        if root is None:
            return False

        return root.val == head.val and (self._dfs(head.next, root.left) or self._dfs(head.next, root.right))

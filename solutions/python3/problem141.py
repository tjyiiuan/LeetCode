# -*- coding: utf-8 -*-
"""
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where the tail connects to.
If pos == -1, then there is no cycle in the linked list.

Follow up
Can you solve it using O(1) (i.e. constant) memory?

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        if head == None:
            return False
        elif head.next == None:
            return False

        s_node = head.next
        f_node = s_node.next

        while s_node != f_node:
            if f_node == None:
                return False
            elif f_node.next == None:
                return False

            s_node = s_node.next
            f_node = f_node.next.next

        return True

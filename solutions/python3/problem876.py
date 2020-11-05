# -*- coding: utf-8 -*-
"""
876. Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Note:

The number of nodes in the given list will be between 1 and 100.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head):
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        count = count // 2

        while count > 0:
            head = head.next
            count -= 1

        return head

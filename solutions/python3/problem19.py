# -*- coding: utf-8 -*-
"""
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head

        res = ListNode(next=head)
        f_node = res
        s_node = res
        while n > 0:
            f_node = f_node.next
            n -= 1

        while f_node.next != None:
            f_node = f_node.next
            s_node = s_node.next

        s_node.next = s_node.next.next

        return res.next

# -*- coding: utf-8 -*-
"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        res = ListNode()
        node = res

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                node.next = ListNode(val=l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(val=l2.val)
                l2 = l2.next
            node = node.next

        if l1 != None:
            l = l1
        else:
            l = l2

        while l != None:
            node.next = ListNode(val=l.val)
            node = node.next
            l = l.next

        return res.next

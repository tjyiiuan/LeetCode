# -*- coding: utf-8 -*-
"""
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head

        res = ListNode(next=head)
        last = head.val

        while head.next != None:
            if head.next.val == last:
                head.next = head.next.next
            else:
                last = head.next.val
                head = head.next

        return res.next

# -*- coding: utf-8 -*-
"""
86. Partition List
Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):
        s_res = ListNode()
        f_res = ListNode()
        s_node = s_res
        f_node = f_res

        while head != None:
            if head.val < x:
                s_node.next = head
                s_node = s_node.next
            else:
                f_node.next = head
                f_node = f_node.next

            head = head.next

        s_node.next = f_res.next
        f_node.next = None

        return s_res.next

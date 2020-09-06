# -*- coding: utf-8 -*-
"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)
        last_node = res

        while last_node.next != None:
            next_node = last_node.next

            if next_node.next == None:
                break

            last_node.next = next_node.next
            next_node.next = last_node.next.next
            last_node.next.next = next_node

            last_node = next_node

        return res.next


# -*- coding: utf-8 -*-
"""
1669. Merge In Between Linked Lists

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.

Constraints:

3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail_index = b + 1
        cur_index = 0
        tail = list1
        while cur_index < tail_index:
            tail = tail.next
            cur_index += 1

        res = ListNode(next=list1)
        head = res
        cur_index = -1
        tar_index = a - 1

        while cur_index < tar_index:
            head = head.next
            cur_index += 1
        head.next = list2

        while head.next:
             head = head.next
        head.next = tail

        return res.next

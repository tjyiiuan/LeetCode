# -*- coding: utf-8 -*-
"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        return self.num_to_list(self.list_to_num(l1) + self.list_to_num(l2))

    def num_to_list(self, num):
        first_node = ListNode(next=ListNode())
        last_node = first_node
        while num > 0:
            digit = num % 10
            num //= 10
            last_node.next = ListNode(digit)
            last_node = last_node.next

        return first_node.next

    def list_to_num(self, l):
        res = l.val
        count = 0

        while l.next is not None:
            count += 1
            l = l.next
            res += l.val * (10 ** count)

        return res
# -*- coding: utf-8 -*-
"""
2181. Merge Nodes in Between Zeros

You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of
the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of
all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

Constraints:

The number of nodes in the list is in the range [3, 2 * 105].
0 <= Node.val <= 1000
There are no two consecutive nodes with Node.val == 0.
The beginning and end of the linked list have Node.val == 0.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_node = ListNode(0)
        cur_node = head_node
        while head and head.next:
            if head.val == 0:
                cur_node.next = ListNode(0)
                cur_node = cur_node.next
            else:
                cur_node.val += head.val

            head = head.next

        return head_node.next

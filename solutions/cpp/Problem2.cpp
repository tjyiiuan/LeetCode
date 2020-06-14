#pragma once
/*
2. Add Two Numbers

You are given two non - empty linked lists representing two non - negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*/

#include <iostream>
#include "Source.h"


class Solution {
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
		ListNode* result = new ListNode(-1);
		ListNode* cur = result;
		int nUp = 0;
		while (l1 != NULL && l2 != NULL)
		{
			int tmp = nUp + l1->val + l2->val;
			nUp = 0;
			cur->next = new ListNode(tmp % 10);
			while (tmp >= 10)
			{
				tmp /= 10;
				nUp += 1;
			}
			cur = cur->next;
			l1 = l1->next;
			l2 = l2->next;
		}
		ListNode* l;
		if (l1 == NULL)
		{
			l = l2;
		}
		else
		{
			l = l1;
		}

		while (l != NULL)
		{
			int tmp = nUp + l->val;
			nUp = 0;
			cur->next = new ListNode(tmp % 10);
			while (tmp >= 10)
			{
				tmp /= 10;
				nUp += 1;
			}
			cur = cur->next;
			l = l->next;
		}

		if (nUp)
		{
			cur->next = new ListNode(nUp);
		}
		return result->next;
	}
	void test() {
		std::vector<int> val0 = { 4, 5, 6 };
		std::vector<int> val1 = { 9, 0, 3 };

		ListNode* node0 = vecToNode(val0);
		ListNode* node1 = vecToNode(val1);
		ListNode* result = addTwoNumbers(node0, node1);
		printListNode(result);
	}
};

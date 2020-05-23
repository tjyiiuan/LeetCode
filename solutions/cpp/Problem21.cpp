#pragma once
/*
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
*/
#include <vector>
#include <iostream>
#include "Source.h"

class Solution21 {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)	{
		ListNode* result = new ListNode(-1);
		ListNode* cur = result;
		while (l1 != NULL && l2 != NULL)
		{
			int val1 = l1->val;
			int val2 = l2->val;
			int val;
			if (val1 < val2)
			{
				l1 = l1->next;
				val = val1;
			}
			else
			{
				l2 = l2->next;
				val = val2;
			}
			cur->next = new ListNode(val);
			cur = cur->next;
		}
		ListNode* l = l1 ? l1 : l2;
		cur->next = l;
		return result->next;
	}
	void test() {
	}
}; 

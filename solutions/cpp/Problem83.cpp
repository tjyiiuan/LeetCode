#pragma once
/*
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.
*/
#include "Source.h"


class Solution83 {
public:
	ListNode* deleteDuplicates(ListNode* head) {
		if (head == NULL)
		{
			return head;
		}

		int last = head->val;
		int curVal = 0;
		ListNode* result = new ListNode(last);
		ListNode* curNode = result;
		while (head != NULL)
		{
			curVal = head->val;
			if (curVal != last)
			{
				curNode->next = new ListNode(curVal);
				curNode = curNode->next;
				last = curVal;
			}
			head = head->next;
		}
		return result;
	}
	void test()	{
		std::vector<int> vecTest = { 1,1,2,3,3,6,6,6,6,6,6,7,9 };
		ListNode* nodeTest = vecToNode(vecTest);
		ListNode* nodeResult = deleteDuplicates(nodeTest);
		printListNode(nodeResult);
	}
};

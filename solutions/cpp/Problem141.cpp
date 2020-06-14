#pragma once
/*
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
*/
#include "Source.h"


class Solution {
public:
	bool hasCycle(ListNode *head) {
		ListNode* fast, *slow;
		if (head == NULL)
		{
			return false;
		}
		else
		{
			slow = head;
			fast = head;
		}
		while (fast && fast->next)
		{
			if (fast->next == NULL)
			{
				return false;
			}
			fast = fast->next->next;
			slow = slow->next;
			if (fast == slow)
			{
				return true;
			}
		}
		return false;
	}
	void test() {

	}
}; 

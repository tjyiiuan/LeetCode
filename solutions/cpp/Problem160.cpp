#pragma once
/*
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:
	If the two linked lists have no intersection at all, return null.
	The linked lists must retain their original structure after the function returns.
	You may assume there are no cycles anywhere in the entire linked structure.
	Your code should preferably run in O(n) time and use only O(1) memory.
*/
#include "Source.h"


class Solution {
public:
	ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
	{
		while (headA != NULL)
		{
			ListNode* listB = headB;
			while (listB != NULL)
			{
				if (headA == listB)
				{
					return headA;
				}
				else
				{
					listB = listB->next;
				}
			}
			headA = headA->next;
		}
		return NULL;
	}
	void test() {

	}
};

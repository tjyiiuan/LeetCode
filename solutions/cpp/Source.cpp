
#include <iostream>
#include "Source.h"


ListNode* vecToNode(std::vector<int> &vecNumber)
{
	ListNode* result = new ListNode(-1);
	ListNode* cur = result;

	for (auto &i : vecNumber)
	{
		cur->next = new ListNode(i);
		cur = cur->next;
	}

	return result->next;
}

void printListNode(ListNode* firstNode)
{
	while (firstNode != NULL)
	{
		std::cout << firstNode->val << "->";
		firstNode = firstNode->next;
	}
	std::cout << std::endl;
}
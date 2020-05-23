#pragma once

#ifndef _SOURCE_H_
#define _SOURCE_H_
#include <vector>

struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

ListNode* vecToNode(std::vector<int> &vecNumber);
void printListNode(ListNode* firstNode);

#endif /* _SOURCE_H_ */
#pragma once
/*
100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
*/
#include "Source.h"


class Solution {
public:
	bool isSameTree(TreeNode* p, TreeNode* q) {
		if (!p && !q) {
			return true;
		}
		else if ((!p && q) || (p && !q) || (p->val != q->val)) {
			return false;
		}
		else {
			return (isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
		}
	}
	void test() {

	}
};

#pragma once
/*
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself(ie, symmetric around its center).
*/
#include "Source.h"


class Solution {
public:
	bool isSymmetric(TreeNode* root) {
		if (!root) {
			return true;
		}
		return isMirror(root->left, root->right);
	}
	bool isMirror(TreeNode* l, TreeNode* r) {
		if (!l && !r) {
			return true;
		}
		else if ((!l && r) || (!r && l) || (l->val != r->val)) {
			return false;
		}
		else {
			return isMirror(l->left, r->right) && isMirror(l->right, r->left);
		}
	}
	void Test() {

	}
};

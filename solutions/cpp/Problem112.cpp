#pragma once
/*
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
*/
#include <vector>
#include "Source.h"


class Solution {
public:
	bool hasPathSum(TreeNode* root, int sum) {
		if (root == NULL) {
			return false;
		}
		std::vector<int> vecResult = allPathSum(root);
		for (std::vector<int>::iterator it = vecResult.begin(); it != vecResult.end(); it++) {
			if (*it == sum) {
				return true;
			}
		}
		return false;
	}
	std::vector<int> allPathSum(TreeNode* root) {
		std::vector<int> lVec, rVec, vecResult;
		TreeNode* lNode = root->left;
		TreeNode* rNode = root->right;

		if (lNode == NULL && rNode == NULL) {
			vecResult = { root->val };
		}
		else {
			if (lNode != NULL) {
				for (auto it : allPathSum(lNode)) {
					lVec.push_back(root->val + it);
				}
			}

			if (rNode != NULL) {
				for (auto it : allPathSum(rNode)) {
					rVec.push_back(root->val + it);
				}
			}

			vecResult.insert(vecResult.end(), lVec.begin(), lVec.end());
			vecResult.insert(vecResult.end(), rVec.begin(), rVec.end());
		}
		return vecResult;
	}
};

#pragma once
/*
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.
*/
#include <vector>
#include <string>
#include "Source.h"


class Solution {
public:
	std::vector<std::string> binaryTreePaths(TreeNode* root) {
		std::vector<std::string> res = {};
		if (!root) {
			return res;
		}
		TreeNode* l = root->left;
		TreeNode* r = root->right;
		std::string v = std::to_string(root->val);
		if (!l && !r) {
			res.push_back(v);
			return res;
		}
		for (auto & path : binaryTreePaths(l)) {
			res.push_back(v + "->" + path);
		}
		for (auto & path : binaryTreePaths(r)) {
			res.push_back(v + "->" + path);
		}
		return res;
	}
};

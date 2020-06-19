#pragma once
/*
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
*/

#include "Source.h"


class Solution {
public:
	int maxDepth(TreeNode* root) {
		if (!root) {
			return 0;
		}
		else {
			int l = maxDepth(root->left);
			int r = maxDepth(root->right);
			return (l > r) ? l + 1 : r + 1;
		}
	}
};
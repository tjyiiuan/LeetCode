#pragma once
/*
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
*/
#include <vector>
#include "Source.h"


class Solution {
public:
	int minDepth(TreeNode* root) {
		if (root == NULL) {
			return 0;
		}
		TreeNode* lNode = root->left;
		TreeNode* rNode = root->right;

		// leaf node
		if (lNode == NULL && rNode == NULL) {
			return 1;
		}
		else if (lNode == NULL && rNode != NULL) {
			return minDepth(rNode) + 1;
		}
		else if (lNode != NULL && rNode == NULL) {
			return minDepth(lNode) + 1;
		}
		else {
			int l = minDepth(lNode);
			int r = minDepth(rNode);
			if (l < r) {
				return l + 1;
			}
			else {
				return r + 1;
			}
		}
	}
};

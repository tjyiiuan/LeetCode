# -*- coding: utf-8 -*-
"""
508. Most Frequent Subtree Sum
Medium

711

133

Add to List

Share
Given the root of a tree, you are asked to find the most frequent subtree sum.
The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node
(including the node itself).
So what is the most frequent subtree sum value?
If there is a tie, return all the values with the highest frequency in any order.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res_dict = {}

    def findFrequentTreeSum(self, root: TreeNode):
        self._get_subtree_sum(root)
        res = []
        count = 0

        for val, cnt in self.res_dict.items():
            if cnt > count:
                count = cnt
                res = [val]
            elif cnt == count:
                res.append(val)

        return res

    def _get_subtree_sum(self, node):
        if node is None:
            return 0

        node_sum = node.val + self._get_subtree_sum(node.left) + self._get_subtree_sum(node.right)

        if node_sum not in self.res_dict:
            self.res_dict[node_sum] = 0
        self.res_dict[node_sum] += 1

        return node_sum

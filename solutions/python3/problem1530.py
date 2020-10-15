# -*- coding: utf-8 -*-
"""
1530. Number of Good Leaf Nodes Pairs

Given the root of a binary tree and an integer distance.
A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path
between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Constraints:
The number of nodes in the tree is in the range [1, 2^10].
Each node's value is between [1, 100].
1 <= distance <= 10
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self._traverse(root, distance)
        return self.res

    def _traverse(self, node, max_dist):
        if node is None:
            return {}

        if node.left is None and node.right is None:
            # leaf
            return {0: 1}

        else:
            leaf_dict = {}
            l_dist_dict = self._traverse(node.left, max_dist)
            r_dist_dict = self._traverse(node.right, max_dist)

            for l_dis, l_node_count in l_dist_dict.items():
                l_dis += 1
                if l_dis not in leaf_dict:
                    leaf_dict[l_dis] = l_node_count
                else:
                    leaf_dict[l_dis] += l_node_count

                for r_dis, r_node_count in r_dist_dict.items():
                    r_dis += 1
                    if l_dis + r_dis <= max_dist:
                        self.res += l_node_count * r_node_count

            for r_dis, node_count in r_dist_dict.items():
                r_dis += 1
                if r_dis not in leaf_dict:
                    leaf_dict[r_dis] = node_count
                else:
                    leaf_dict[r_dis] += node_count

            return leaf_dict

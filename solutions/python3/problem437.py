# -*- coding: utf-8 -*-
"""
437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> int:
        res = 0
        stack = [({}, root)]
        while stack:
            path_sum, node = stack.pop()
            if node is None:
                continue

            cur_sum = {}

            for val, count in path_sum.items():
                val += node.val
                cur_sum[val] = count

            if node.val not in cur_sum:
                cur_sum[node.val] = 1
            else:
                cur_sum[node.val] += 1

            for val, count in cur_sum.items():
                if val == target_sum:
                    res += count

            stack.append((cur_sum, node.left))
            stack.append((cur_sum, node.right))

        return res

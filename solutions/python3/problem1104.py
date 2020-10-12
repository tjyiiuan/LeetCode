# -*- coding: utf-8 -*-
"""
1104. Path In Zigzag Labelled Binary Tree

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node
with that label.


Constraints:
1 <= label <= 10^6
"""


class Solution:
    def pathInZigZagTree(self, label: int):
        raw_res = []
        tmp_label = label
        while tmp_label != 1:
            tmp_label = tmp_label // 2
            raw_res.append(tmp_label)

        tmp_sum = 3
        index = len(raw_res) - 1
        need_reverse = index % 2 == 0
        res = []
        while index >= 0:
            if need_reverse:
                one_label = tmp_sum - 1 - raw_res[index]
            else:
                one_label = raw_res[index]

            res.append(one_label)
            index -= 1
            tmp_sum *= 2
            need_reverse = not need_reverse

        return res + [label]

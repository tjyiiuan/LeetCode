# -*- coding: utf-8 -*-
"""
1506. Find Root of N-Ary Tree

You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value.

Return the root of the N-ary tree.

Custom testing:

An N-ary tree can be serialized as represented in its level order traversal where each group of children is separated
by the null value (see examples).

The testing will be done in the following way:

The input data should be provided as a serialization of the tree.
The driver code will construct the tree from the serialized input data and put each Node object into an array in
an arbitrary order.
The driver code will pass the array to findRoot, and your function should find and return the root Node object
in the array.
The driver code will take the returned Node object and serialize it.
If the serialized value and the input data are the same, the test passes.

Constraints:

The total number of nodes is between [1, 5 * 104].
Each node has a unique value.

Follow up:

Could you solve this problem in constant space complexity with a linear time algorithm?
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree):
        val_sum = 0

        for node in tree:
            val_sum += node.val - sum(n.val for n in node.children)

        for node in tree:
            if val_sum == node.val:
                return node

# -*- coding: utf-8 -*-
"""
1490. Clone N-ary Tree

Given a root of an N-ary tree, return a deep copy (clone) of the tree.

Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

class Node {
    public int val;
    public List<Node> children;
}
Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Follow up: Can your solution work for the graph problem?

Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 10^4].
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return

        return Node(val=root.val, children=[self.cloneTree(node) for node in root.children])

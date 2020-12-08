# -*- coding: utf-8 -*-
"""
1650. Lowest Common Ancestor of a Binary Tree III

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia:
"The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants
(where we allow a node to be a descendant of itself)."

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.
"""


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_anc_set = {p.val}
        while p.parent:
            p = p.parent
            p_anc_set.add(p.val)

        while q:
            if q.val in p_anc_set:
                return q
            else:
                q = q.parent

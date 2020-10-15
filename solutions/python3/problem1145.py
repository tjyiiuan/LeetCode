# -*- coding: utf-8 -*-
"""
1145. Binary Tree Coloring Game

Two players play a turn based game on a binary tree.
We are given the root of this binary tree, and the number of nodes n in the tree.
n is odd, and each node has a distinct value from 1 to n.

Initially, the first player names a value x with 1 <= x <= n,
and the second player names a value y with 1 <= y <= n and y != x.
The first player colors the node with value x red, and the second player colors the node with value y blue.

Then, the players take turns starting with the first player.
In each turn, that player chooses a node of their color (red if player 1, blue if player 2)
and colors an uncolored neighbor of the chosen node (either the left child, right child,
or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn.
If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.
If it is not possible, return false.


Constraints:

root is the root of a binary tree with n nodes and distinct node values from 1 to n.
n is odd.
1 <= x <= n <= 100
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root, n, x):
        # find node x
        stack = [root]
        while True:
            node = stack.pop()
            if node is None:
                continue
            if node.val == x:
                # node x
                break
            else:
                stack.append(node.left)
                stack.append(node.right)

        l_count = self._count_node(node.left)
        r_count = self._count_node(node.right)
        p_count = n - l_count - r_count - 1

        return max(l_count, r_count, p_count) * 2 > n

    def _count_node(self, node):
        if node is None:
            return 0

        return self._count_node(node.left) + self._count_node(node.right) + 1

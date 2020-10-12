# -*- coding: utf-8 -*-
"""
889. Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

Note:
1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, pre, post) -> TreeNode:
        length = len(pre)
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(val=pre[0])
        elif length == 2:
            return TreeNode(val=pre[0], left=TreeNode(val=pre[1]))
        elif pre[1] == post[-2]:
            return TreeNode(val=pre[0], left=self.constructFromPrePost(pre[1:], post[:-1]))
        else:
            l_val = pre[1]
            r_val = post[-2]

            # build left and right pre
            pre_ind = pre.index(r_val)
            l_pre = pre[1:pre_ind]
            r_pre = pre[pre_ind:]

            # build left and right post
            post_ind = post.index(l_val)
            l_post = post[:post_ind + 1]
            r_post = post[post_ind + 1:-1]

            left = self.constructFromPrePost(l_pre, l_post)
            right = self.constructFromPrePost(r_pre, r_post)
            return TreeNode(val=pre[0], left=left, right=right)

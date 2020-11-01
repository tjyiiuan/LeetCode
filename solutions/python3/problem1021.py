# -*- coding: utf-8 -*-
"""
1021. Remove Outermost Parentheses

A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
where A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B,
with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k,
where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
"""


class Solution:
    def removeOuterParentheses(self, string: str) -> str:
        count = 0
        last_start = 0
        res_ind = []
        for ind, char in enumerate(string):
            if char == ")":
                count -= 1
            else:
                count += 1

            if count == 0:
                res_ind.append([last_start, ind])
                last_start = ind + 1

        res = ""
        for start_ind, end_ind in res_ind:
            res += string[start_ind + 1:end_ind]

        return res

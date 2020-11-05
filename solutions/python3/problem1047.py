# -*- coding: utf-8 -*-
"""
1047. Remove All Adjacent Duplicates In String

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters,
and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
"""


class Solution:
    def removeDuplicates(self, string: str) -> str:
        max_ind = len(string) - 1
        ind = 0
        while ind < max_ind:
            if ind < 0:
                ind = 0
            elif string[ind] == string[ind + 1]:
                string = string[:ind] + string[ind + 2:]
                max_ind -= 2
                ind -= 1
            else:
                ind += 1

        return string

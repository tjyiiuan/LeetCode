# -*- coding: utf-8 -*-
"""
650. 2 Keys Keyboard

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.
Note:

The n will be in the range [1, 1000].
"""


class Solution:
    def minSteps(self, n: int) -> int:
        step = 0
        s = 2
        while n > 1:
            while n % s == 0:
                n //= s
                step += s
            s += 1

        return step

s = Solution()
print(s.minSteps(27))


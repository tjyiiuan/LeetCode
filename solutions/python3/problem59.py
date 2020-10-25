# -*- coding: utf-8 -*-
"""
59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
"""


class Solution:
    def generateMatrix(self, n):
        res = [[0] * n for i in range(n)]

        min_row = 0
        min_col = 0
        max_row = n - 1
        max_col = n - 1

        cur_row = 0
        cur_col = 0
        cur_val = 1
        max_val = n ** 2

        direction = "right"
        while cur_val <= max_val:
            res[cur_row][cur_col] = cur_val
            cur_val += 1
            if direction == "right":
                if cur_col == max_col:
                    min_row += 1
                    cur_row += 1
                    direction = "down"
                else:
                    cur_col += 1
            elif direction == "down":
                if cur_row == max_row:
                    max_col -= 1
                    cur_col -= 1
                    direction = "left"
                else:
                    cur_row += 1
            elif direction == "left":
                if cur_col == min_col:
                    max_row -= 1
                    cur_row -= 1
                    direction = "up"
                else:
                    cur_col -= 1
            elif direction == "up":
                if cur_row == min_row:
                    min_col += 1
                    cur_col += 1
                    direction = "right"
                else:
                    cur_row -= 1

        return res

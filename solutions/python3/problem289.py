# -*- coding: utf-8 -*-
"""
289. Game of Life

According to the Wikipedia's article:
"The Game of Life, also known simply as Life, is a cellular automaton devised
by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array.

In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array.
How would you address these problems?
"""


import copy


class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        matrix = copy.deepcopy(board)
        row_max = len(matrix)
        col_max = len(matrix[0])

        for r_ind, row in enumerate(matrix):
            new_row = []
            for c_ind, val in enumerate(row):
                count = - val

                for cur_row_ind in [r_ind - 1, r_ind, r_ind + 1]:
                    if cur_row_ind < 0 or cur_row_ind >= row_max:
                        continue
                    for cur_col_ind in [c_ind - 1, c_ind, c_ind + 1]:
                        if cur_col_ind < 0 or cur_col_ind >= col_max:
                            continue

                        count += matrix[cur_row_ind][cur_col_ind]

                if val == 0:
                    if count == 3:
                        new_status = 1
                    else:
                        new_status = 0
                else:
                    if 2 <= count <= 3:
                        new_status = 1
                    else:
                        new_status = 0

                board[r_ind][c_ind] = new_status

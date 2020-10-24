# -*- coding: utf-8 -*-
"""
999. Available Captures for Rook

On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.
These are given as characters 'R', '.', 'B', and 'p' respectively.
Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
then moves in that direction until it chooses to stop, reaches the edge of the board,
or captures an opposite colored pawn by moving to the same square it occupies.
Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Note:

board.length == board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
"""


class Solution:
    def numRookCaptures(self, board) -> int:
        res = 0

        for r_ind, row in enumerate(board):
            try:
                c_ind = row.index("R")
            except ValueError:
                continue

            # left
            cur_c = c_ind - 1
            while cur_c >= 0:
                if row[cur_c] == ".":
                    pass
                else:
                    if row[cur_c] == "p":
                        res += 1
                    break
                cur_c -= 1

            # right
            cur_c = c_ind + 1
            while cur_c <= 7:
                if row[cur_c] == ".":
                    pass
                else:
                    if row[cur_c] == "p":
                        res += 1
                    break
                cur_c += 1

            # up
            cur_r = r_ind - 1
            while cur_r >= 0:
                if board[cur_r][c_ind] == ".":
                    pass
                else:
                    if board[cur_r][c_ind] == "p":
                        res += 1
                    break
                cur_r -= 1

            # down
            cur_r = r_ind + 1
            while cur_r <= 7:
                if board[cur_r][c_ind] == ".":
                    pass
                else:
                    if board[cur_r][c_ind] == "p":
                        res += 1
                    break
                cur_r += 1

            return res

# -*- coding: utf-8 -*-
"""
1222. Queens That Can Attack the King

On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of the Black Queens,
and a pair of coordinates king that represent the position of the White King,
return the coordinates of all the queens (in any order) that can attack the King.

Constraints:

1 <= queens.length <= 63
queens[0].length == 2
0 <= queens[i][j] < 8
king.length == 2
0 <= king[0], king[1] < 8
At most one piece is allowed in a cell.
"""


class Solution:
    def queensAttacktheKing(self, queens, king):
        max_ind = 7
        res = []
        queen_set = set(tuple(q) for q in queens)
        king_i, king_j = king

        # left
        cur_i = king_i - 1
        while cur_i >= 0:
            cur_king = (cur_i, king_j)
            if cur_king in queen_set:
                res.append(list(cur_king))
                break
            cur_i -= 1

        # right
        cur_i = king_i + 1
        while cur_i <= max_ind:
            cur_king = (cur_i, king_j)
            if cur_king in queen_set:
                res.append(list(cur_king))
                break
            cur_i += 1

        # up
        cur_j = king_j - 1
        while cur_j >= 0:
            cur_king = (king_i, cur_j)
            if cur_king in queen_set:
                res.append(list(cur_king))
                break
            cur_j -= 1

        # down
        cur_j = king_j + 1
        while cur_j <= max_ind:
            cur_king = (king_i, cur_j)
            if cur_king in queen_set:
                res.append(list(cur_king))
                break
            cur_j += 1

        # diag1
        cur_i = king_i + 1
        cur_j = king_j + 1
        while cur_i <= max_ind and cur_j <= max_ind:
            cur_king = (cur_i, cur_j)
            if cur_king in queen_set:
                res.append(list(cur_king))
                break
            cur_i += 1
            cur_j += 1

        # diag2
        cur_i = king_i + 1
        cur_j = king_j - 1
        while cur_i <= max_ind and cur_j >= 0:
            cur_king = (cur_i, cur_j)
            if cur_king in queen_set:
                res.append(list(cur_king))
                break
            cur_i += 1
            cur_j -= 1

        # diag3
        cur_i = king_i - 1
        cur_j = king_j + 1
        while cur_i >= 0 and cur_j <= max_ind:
            cur_king = (cur_i, cur_j)
            if cur_king in queen_set:
                res.append(list(cur_king))
                break
            cur_i -= 1
            cur_j += 1

        # diag4
        cur_i = king_i - 1
        cur_j = king_j - 1
        while cur_i >= 0 and cur_j >= 0:
            cur_king = (cur_i, cur_j)
            if cur_king in queen_set:
                res.append(list(cur_king))
                break
            cur_i -= 1
            cur_j -= 1

        return res

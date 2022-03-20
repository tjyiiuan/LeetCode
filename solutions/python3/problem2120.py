# -*- coding: utf-8 -*-
"""
2120. Execution of All Suffix Instructions Staying in a Grid

There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). You are given the
integer n and an integer array startPos where startPos = [startrow, startcol] indicates that a robot is initially at
cell (startrow, startcol).

You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L' (move left),
'R' (move right), 'U' (move up), and 'D' (move down).

The robot can begin executing from any ith instruction in s. It executes the instructions one by one towards the end of
s but it stops if either of these conditions is met:

The next instruction will move the robot off the grid.
There are no more instructions left to execute.
Return an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot
begins executing from the ith instruction in s.

Constraints:

m == s.length
1 <= n, m <= 500
startPos.length == 2
0 <= startrow, startcol < n
s consists of 'L', 'R', 'U', and 'D'.
"""


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        for i in range(len(s)):
            cur_pos = startPos[:]
            move_count = 0
            for move in s[i:]:
                # move
                if move == "R":
                    cur_pos[1] += 1
                elif move == "L":
                    cur_pos[1] -= 1
                elif move == "U":
                    cur_pos[0] -= 1
                else:
                    cur_pos[0] += 1

                # valid
                if cur_pos[0] < 0 or cur_pos[0] >= n or cur_pos[1] < 0 or cur_pos[1] >= n:
                    break
                else:
                    move_count += 1

            result.append(move_count)

        return result

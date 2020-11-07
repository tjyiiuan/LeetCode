# -*- coding: utf-8 -*-
"""
657. Robot Return to Origin
Easy

1095

681

Add to List

Share
There is a robot starting at position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move.
Valid moves are R (right), L (left), U (up), and D (down).
If the robot returns to the origin after it finishes all of its moves, return true.
Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant.
"R" will always make the robot move to the right once, "L" will always make it move left, etc.
Also, assume that the magnitude of the robot's movement is the same for each move.

Constraints:

1 <= moves.length <= 2 * 104
moves only contains the characters 'U', 'D', 'L' and 'R'.
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hori_count = 0
        vert_count = 0
        for char in moves:
            if char == "R":
                hori_count += 1
            elif char == "L":
                hori_count -= 1
            elif char == "U":
                vert_count += 1
            elif char == "D":
                vert_count -= 1

        return hori_count == 0 and vert_count == 0

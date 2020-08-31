# -*- coding: utf-8 -*-
"""
1025. Divisor Game

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.


Note:
1 <= N <= 1000
"""


class Solution:
    def __init__(self):
        self.cache = {1: False, 2: True, 3:False}

    def divisorGame(self, N: int) -> bool:
        if N not in self.cache:
            result = False
            i = int(N ** 0.5)
            while i > 0:
                if N % i == 0:
                    if not self.divisorGame(N - i):
                        result = True
                        break
                i -= 1

            self.cache[N] = result

        return self.cache[N]



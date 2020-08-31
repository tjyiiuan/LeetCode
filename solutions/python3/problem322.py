# -*- coding: utf-8 -*-
"""
322. Coin Change

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def __init__(self):
        self.cache = {0: 0}

    def coinChange(self, coins, amount):
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        if amount in self.cache:
            return self.cache[amount]

        coins = sorted(coins)
        coin = 1
        while coin <= amount:
            if coin in coins:
                count = 1
            else:
                tmp = []
                for i in coins[::-1]:
                    res = coin - i
                    if res < 0:
                        continue
                    c = self.cache[res]
                    if c > 0:
                        tmp.append(c)
                if tmp == []:
                    count = -1
                else:
                    count = min(tmp) + 1

            self.cache[coin] = count
            coin += 1

        return self.cache[amount]

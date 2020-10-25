# -*- coding: utf-8 -*-
"""
122. Best Time to Buy and Sell Stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4
"""


class Solution:
    def maxProfit(self, prices):
        res = 0
        for ind in range(1, len(prices)):
            profit = prices[ind] - prices[ind - 1]
            if profit > 0:
                res += profit

        return res

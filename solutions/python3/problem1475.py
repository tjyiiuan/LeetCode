# -*- coding: utf-8 -*-
"""
1475. Final Prices With a Special Discount in a Shop

Given the array prices where prices[i] is the price of the ith item in a shop.
There is a special discount for items in the shop, if you buy the ith item,
then you will receive a discount equivalent to prices[j] where j is the minimum index
such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop
considering the special discount.

Constraints:

1 <= prices.length <= 500
1 <= prices[i] <= 10^3
"""


class Solution:
    def finalPrices(self, prices):
        res = []
        for ind in range(len(prices) - 1):
            b_dis = False
            for dis_ind in range(ind + 1, len(prices)):
                if prices[dis_ind] <= prices[ind]:
                    res.append(prices[ind] - prices[dis_ind])
                    b_dis = True
                    break
            if not b_dis:
                res.append(prices[ind])

        res.append(prices[-1])

        return res

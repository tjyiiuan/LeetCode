#pragma once
/*
122. Best Time to Buy and Sell Stock II

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
*/
#include <iostream>
#include <vector>
#include "Source.h"


class Solution {
public:
	int maxProfit(std::vector<int>& prices) {
		int profit = 0, diff;
		for (int i = 0; i < prices.size() - 1; i++) {
			diff = prices[i + 1] - prices[i];
			if (diff > 0) {
				profit += diff;
			}
		}
		return profit;
	}
	void test() {
		std::vector<int> prices = { 7,1,5,3,6,4 };
		std::cout << maxProfit(prices) << std::endl;
	}
};
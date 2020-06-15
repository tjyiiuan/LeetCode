#pragma once
/*
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
*/
#include <iostream>
#include <vector>
#include "Source.h"


class Solution {
public:
	int maxProfit(std::vector<int>& prices) {
		int profit = 0, days = prices.size();
		if (days < 2) {
			return profit;
		}
		int buy = prices[0], diff;
		for (int sell = 0; sell < days; sell++) {
			if (prices[sell] <= buy) {
				buy = prices[sell];
			}
			else {
				diff = prices[sell] - buy;
				if (diff > profit) {
					profit = diff;
				}
			}
		}
		return profit;
	}
	int maxProfitSlow(std::vector<int>& prices) {
		int profit = 0;
		int days = prices.size();
		if (days < 2) {
			return profit;
		}
		for (int buy = 0; buy < days - 1; buy++) {
			for (int sell = buy + 1; sell < days; sell++) {
				int diff = prices[sell] - prices[buy];
				if (diff > profit) {
					profit = diff;
				}
			}
		}
		return profit;
	}
	void test() {
		std::vector<int> prices = { 7,1,5,3,6,4 };
		std::cout << maxProfit(prices) <<std::endl;
	}
};
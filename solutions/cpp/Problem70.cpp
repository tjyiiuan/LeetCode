#pragma once
/*
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
*/
#include <iostream>
#include <map>


class Solution {
public:
	Solution() {
		cache[1] = 1;
		cache[2] = 2;
	}
	int climbStairs(int n) {
		if (cache.find(n) == cache.end())
		{
			int method = climbStairs(n - 1) + climbStairs(n - 2);
			cache[n] = method;
		}
		return cache[n];
	}
	void test()
	{
		for (int i = 1; i < 10; i++)
		{
			std::cout << climbStairs(i) << std::endl;
		}
	}
private:
	std::map<int, int> cache;
};

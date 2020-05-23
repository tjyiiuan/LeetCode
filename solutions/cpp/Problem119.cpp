#pragma once
/*
119. Pascal's Triangle II

Given a non-negative index k where k <= 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
*/
#include <iostream>
#include <vector>


class Solution119 {
public:
	std::vector<int> getRow(int rowIndex) {
		std::vector<int> res = { 1 };
		if (rowIndex == 0)
		{
			return res;
		}
		if (rowIndex == 1)
		{
			res.push_back(1);
		}
		else
		{
			std::vector<int> last = getRow(rowIndex - 1);
			for (int i = 0; i < last.size() - 1; i++)
			{
				res.push_back(last[i] + last[i + 1]);
			}
			res.push_back(1);
		}
		return res;
	}
	void test()	{
		int num = 5;
		for (auto &i : getRow(num))
		{
			std::cout << i << " ";
		}
		std::cout << std::endl;
	}
}; 

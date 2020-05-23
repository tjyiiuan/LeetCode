#pragma once
/*
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
*/
#include <iostream>
#include <vector>


class Solution118 {
public:
	std::vector<std::vector<int>> generate(int numRows) {
		std::vector<std::vector<int>> res;
		if (numRows >= 1)
		{
			std::vector<int> vec = { 1 };
			res.push_back(vec);
		}

		if (numRows >= 2)
		{
			std::vector<int> vec = { 1, 1 };
			res.push_back(vec);
		}

		if (numRows > 2)
		{
			for (int i = 2; i < numRows; i++)
			{
				std::vector<int> last = res[i - 1];
				std::vector<int> vec = { 1 };
				for (int j = 0; j < last.size() - 1; j++)
				{
					vec.push_back(last[j] + last[j + 1]);
				}
				vec.push_back(1);
				res.push_back(vec);
			}
		}

		return res;
	}
	void test()	{
		int num = 8;
		for (auto &i : generate(num))
		{
			for (auto &j : i)
			{
				std::cout << j << " ";
			}
			std::cout << std::endl;
		}
	}
};

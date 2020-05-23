#pragma once
/*
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
*/
#include <iostream>
#include <string>
#include <vector>


class Solution14 {
public:
	std::string longestCommonPrefix(std::vector<std::string>& strs)	{
		std::string comPrefix;
		if (strs.empty()) return comPrefix;
		for (int i = 0; i < strs[0].size(); i++) {
			for (int j = 1; j < strs.size(); j++) {
				if (i >= strs[j].size() || strs[j][i] != strs[0][i])
					return comPrefix;
			}
			comPrefix.push_back(strs[0][i]);
		}
		return comPrefix;
	}
	void test() {
		std::vector<std::string> strs;
		strs.push_back("flower");
		strs.push_back("flow");
		strs.push_back("flight");
		std::cout << longestCommonPrefix(strs) << std::endl;
	}

};

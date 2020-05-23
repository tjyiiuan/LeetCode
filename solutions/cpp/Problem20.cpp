#pragma once
/*
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
*/
#include <iostream>
#include <map>
#include <stack>
#include <string>


class Solution20 {
public:
	Solution20()
	{
		for (int i = 0; i < 3; i++)
		{
			std::string bra = "([{)]}";
			braMap[bra[i]] = bra[i + 3];
		}
	}
	bool isValid(std::string s) {
		std::stack<char> cache;
		for (auto &ch : s)
		{
			if (braMap.find(ch) != braMap.end())
			{
				cache.push(ch);
			}
			else
			{
				if (cache.empty())
				{
					return false;
				}
				char cur = cache.top();
				if (braMap[cur] != ch)
				{
					return false;
				}
				else
				{
					cache.pop();
				}
			}
		}
		if (!cache.empty())
		{
			return false;
		}
		return true;
	}
	void test()	{
		std::cout << isValid("{[]}") << std::endl; // true
		std::cout << isValid("([)]") << std::endl; // false
		std::cout << isValid("()[]{}") << std::endl; // true
		std::cout << isValid("") << std::endl; // true
		std::cout << isValid("]") << std::endl; // false
	}
private:
	std::map<char, char> braMap;
}; 


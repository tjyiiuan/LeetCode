#pragma once
/*
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
*/
#include <iostream>
#include <string>


class Solution {
public:
	bool isPalindrome(std::string s)
	{
		if (s == "")
		{
			return true;
		}
		int first = 0;
		int last = s.size();
		while (first < last)
		{
			if (convertChar(s[first]) == 0)
			{
				//std::cout << "First not a char!" <<s[first] << std::endl;
				first++;
			}
			else if (convertChar(s[last]) == 0)
			{
				//std::cout << "Last not a char!" << s[last] << std::endl;
				last--;
			}
			else if (convertChar(s[first]) == convertChar(s[last]))
			{
				first++;
				last--;
			}
			else
			{
				return false;
			}
		}

		return true;
	}
	char convertChar(char ch) {
		if (ch >= 'a' && ch <= 'z')
		{
			return ch;
		}
		else if (ch >= 'A' && ch <= 'Z')
		{
			return ch + 32;
		}
		else if (ch >= '0' && ch <= '9')
		{
			return ch;
		}
		else
		{
			return 0;
		}
	}
	void test()	{
		std::cout << isPalindrome("race a car") << std::endl;
		std::cout << isPalindrome("A man, a plan, a canal: Panama") << std::endl;
		std::cout << isPalindrome("0P") << std::endl;
	}
};

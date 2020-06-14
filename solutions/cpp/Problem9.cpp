#pragma once
/*
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
*/
#include <iostream>


class Solution {
public:
	bool isPalindrome(int x) {
		if (x < 0)
		{
			return false;
		}
		else
		{
			return (reverse(x) == x);
		}
	}
	int reverse(int x) {
		long long result = 0;
		while (x != 0)
		{
			result *= 10;
			result += x % 10;
			x /= 10;
		}
		if (result > INT_MAX || result < INT_MIN)
		{
			return 0;
		}
		return (int)result;
	}
	void test()	{
		std::cout << "isPalindrome 38466483: " << isPalindrome(38466483) << std::endl;
		std::cout << "isPalindrome -141: " << isPalindrome(-141) << std::endl;
		std::cout << "isPalindrome 2147483648: " << isPalindrome(2147483648) << std::endl;
	}
};

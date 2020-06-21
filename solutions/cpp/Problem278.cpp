#pragma once
/*
278. First Bad Version

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. 
You should minimize the number of calls to the API.
*/
#include <iostream>


class Solution {
public:
	int firstBadVersion(int n) {
		if (isBadVersion(1)) {
			return 1;
		}
		int first = 1, last = n;
		int tmp;
		while (last > first) {
			tmp = first + (last - first) / 2;
			if (isBadVersion(tmp)) {
				last = tmp;
			}
			else {
				first = tmp + 1;
			}
		}
		return first;
	}
	bool isBadVersion(int version) {
		this->callCount += 1;
		return (version == 1702766719);
	}
	void test() {
		this->callCount = 0;
		std::cout << firstBadVersion(2126753390) << std::endl;
		std::cout << "API called " << this->callCount << " times." << std::endl;
	}
private:
	int callCount = 0;
};

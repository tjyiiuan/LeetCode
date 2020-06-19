#pragma once
/*
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
*/
#include <vector>


class Solution {
public:
	void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
		int index = m + n;
		int num1, num2;
		--m;
		--n;
		while (m >= 0 and n >= 0) {
			num1 = nums1[m];
			num2 = nums2[n];
			if (num1 > num2) {
				nums1[--index] = num1;
				--m;
			}
			else {
				nums1[--index] = num2;
				--n;
			}
		}
		if (n >= 0) {
			for (int i = n; i >= 0;) {
				nums1[i--] = nums2[i];
			}
		}
	}
	void test() {

	}
}; 


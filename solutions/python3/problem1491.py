# -*- coding: utf-8 -*-
"""
1491. Average Salary Excluding the Minimum and Maximum Salary

Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.

Constraints:

3 <= salary.length <= 100
10^3 <= salary[i] <= 10^6
salary[i] is unique.
Answers within 10^-5 of the actual value will be accepted as correct.
"""


class Solution:
    def average(self, salary) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)

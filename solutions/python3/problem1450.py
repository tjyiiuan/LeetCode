# -*- coding: utf-8 -*-
"""
1450. Number of Students Doing Homework at a Given Time

Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally,
return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

Constraints:

startTime.length == endTime.length
1 <= startTime.length <= 100
1 <= startTime[i] <= endTime[i] <= 1000
1 <= queryTime <= 1000
"""


class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        res = 0
        for s_time, e_time in zip(startTime, endTime):
            if s_time <= queryTime <= e_time:
                res += 1

        return res

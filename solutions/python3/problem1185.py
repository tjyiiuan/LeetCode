# -*- coding: utf-8 -*-
"""
1185. Day of the Week

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
"Saturday"}.

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""


from datetime import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        diff = 365 * year + sum(month_day[:month - 1]) + day
        diff += year // 4 - year // 100 + year // 400

        if (year % 4 == 0 and year % 100 !=0 or year % 400 == 0) and month < 3:
            diff -= 1

        return weekday[diff % 7 - 1]

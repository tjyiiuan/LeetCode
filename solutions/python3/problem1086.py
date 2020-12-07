# -*- coding: utf-8 -*-
"""
1086. High Five

Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from
a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents
the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5
using integer division.

Constraints:

1 <= items.length <= 1000
items[i].length == 2
1 <= IDi <= 1000
0 <= scorei <= 100
For each IDi, there will be at least five scores.
"""


class Solution:
    def highFive(self, items):
        cache = {}
        for sid, score in items:
            if sid not in cache:
                cache[sid] = [score]
            else:
                cache[sid].append(score)

        return [[sid, sum(sorted(cache[sid])[-5:]) // 5] for sid in sorted(cache.keys())]

# -*- coding: utf-8 -*-
"""
1817. Finding the Users Active Minutes

You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array
logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed
an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of
users whose UAM equals j.

Return the array answer as described above.

Constraints:

1 <= logs.length <= 104
0 <= IDi <= 109
1 <= timei <= 105
k is in the range [The maximum UAM for a user, 105].
"""


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_dict = {}
        for user, time in logs:
            if user not in user_dict:
                user_dict[user] = set()
            user_dict[user].add(time)

        result = [0] * k
        for _, time_set in user_dict.items():
            result[len(time_set) - 1] += 1

        return result

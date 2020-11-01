# -*- coding: utf-8 -*-
"""
933. Number of Recent Calls

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds,
and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Constraints:

1 <= t <= 109
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.
"""


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
class RecentCounter:
    def __init__(self):
        self.cache = []

    def ping(self, t: int) -> int:
        last_time = t - 3000
        self.cache.append(t)
        new_cache = [ping for ping in self.cache if ping >= last_time]
        self.cache = new_cache
        return len(self.cache)

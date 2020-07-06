# -*- coding: utf-8 -*-


class Solution:
    def isHappy(self, n: int) -> bool:
        func = lambda x: sum(int(i) ** 2 for i in str(x))
        cache = set()
        while True:
            if n == 1:
                return True
            elif n not in cache:
                cache.add(n)
                n = func(n)
            else:
                return False

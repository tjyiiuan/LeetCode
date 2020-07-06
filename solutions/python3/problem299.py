# -*- coding: utf-8 -*-


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict = {}
        guess_list = []
        bull = 0
        cow = 0
        for index, s_char in enumerate(secret):
            g_char = guess[index]
            if g_char == s_char:
                bull += 1
            else:
                guess_list.append(g_char)
                if s_char not in secret_dict:
                    secret_dict[s_char] = 0
                secret_dict[s_char] += 1

        for g_char in guess_list:
            if g_char in secret_dict and secret_dict[g_char] != 0:
                cow += 1
                secret_dict[g_char] -= 1

        return f"{bull}A{cow}B"

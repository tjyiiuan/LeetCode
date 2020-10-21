# -*- coding: utf-8 -*-
"""
950. Reveal Cards In Increasing Order

In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.

Note:

1 <= A.length <= 1000
1 <= A[i] <= 10^6
A[i] != A[j] for all i != j
"""


class Solution:
    def deckRevealedIncreasing(self, deck):
        sorted_dek = sorted(deck)[::-1]
        res = []
        for val in sorted_dek[:-1]:
            res.insert(0, val)
            res.insert(0, res.pop())

        return [sorted_dek[-1]] + res

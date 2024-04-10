# 950. Reveal Cards In Increasing Order
# https://leetcode.com/problems/reveal-cards-in-increasing-order/

from typing import List
from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        result = [0] * n
        queue = deque(range(n))
        index = 0
        
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        
        return result
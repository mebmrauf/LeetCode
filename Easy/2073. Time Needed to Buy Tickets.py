# 2073. Time Needed to Buy Tickets
# https://leetcode.com/problems/time-needed-to-buy-tickets/

from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        result = 0
        for i in range(n):
            if i <= k:
                result += min(tickets[i], tickets[k])
            else:
                result += min(tickets[i], tickets[k] - 1)
        return result
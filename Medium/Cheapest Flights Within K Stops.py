# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [[float("inf")] * n for i in range(k + 2)]
        f[0][src] = 0

        for t in range(1, k + 2):
            for i, j, cost in flights:
                f[t][j] = min(f[t][j], f[t - 1][i] + cost)
        
        result = min(f[t][dst] for t in range(1, k + 2))
        
        return -1 if result == float("inf") else result
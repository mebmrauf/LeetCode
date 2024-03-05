# 1642. Furthest Building You Can Reach
# https://leetcode.com/problems/furthest-building-you-can-reach/description/

from queue import PriorityQueue
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = PriorityQueue()
        i = 0
        
        while i < len(heights) - 1:
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                pq.put(diff)
                if pq.qsize() > ladders:
                    bricks -= pq.get()  
                if bricks < 0:
                    return i    
            i += 1
            
        return i
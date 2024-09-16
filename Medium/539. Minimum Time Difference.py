# 539. Minimum Time Difference
# https://leetcode.com/problems/minimum-time-difference/

from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timeToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        minutes = sorted(timeToMinutes(time) for time in timePoints)
        minDiff = float('inf')
        
        for i in range(len(minutes) - 1):
            minDiff = min(minDiff, minutes[i + 1] - minutes[i])

        minDiff = min(minDiff, (1440 - minutes[-1]) + minutes[0])
        
        return minDiff
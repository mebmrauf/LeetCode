# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        
        result, i = [], 0
        start, end = newInterval
        
        # Add all intervals ending before newInterval starts
        while i < len(intervals) and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1
        
        # Merge intervals overlapping with newInterval
        while i < len(intervals) and intervals[i][0] <= end:
            start, end = min(start, intervals[i][0]), max(end, intervals[i][1])
            i += 1
        result.append([start, end])
        
        # Add all remaining intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result
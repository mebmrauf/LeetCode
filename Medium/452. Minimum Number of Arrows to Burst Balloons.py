# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        result = len(points)
        prev = points[0]
        for i in range(1, len(points)):
            current = points[i]
            if current[0] <= prev[1]:
                result -= 1
                prev = [current[0], min(current[1], prev[1])]
            else:
                prev = current
        return result
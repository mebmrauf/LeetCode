# 1765. Map of Highest Peak
# https://leetcode.com/problems/map-of-highest-peak/

from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))

        directions = [ (0,1), (1, 0), (0, -1), (-1, 0) ]

        while queue:
            posX, posY = queue.popleft()

            for dirX, dirY in directions:
                nposX, nposY = posX + dirX, posY + dirY

                if 0 <= nposX < m and 0 <= nposY < n and height[nposX][nposY] == -1:
                    height[nposX][nposY] = height[posX][posY] + 1
                    queue.append((nposX, nposY))

        return height
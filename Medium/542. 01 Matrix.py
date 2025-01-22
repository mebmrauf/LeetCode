# 542. 01 Matrix
# https://leetcode.com/problems/01-matrix/

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        distance = [[-1] * n for _ in range(m)]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    queue.append((i, j))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


        while queue:
            posX, posY = queue.popleft()

            for dirX, dirY in directions:
                nposX, nposY = posX + dirX, posY + dirY

                if 0 <= nposX < m and 0 <= nposY < n and distance[nposX][nposY] == -1:
                    distance[nposX][nposY] = distance[posX][posY] + 1
                    queue.append((nposX, nposY))

        return distance
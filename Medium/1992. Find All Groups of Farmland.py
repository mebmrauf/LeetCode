# 1992. Find All Groups of Farmland
# https://leetcode.com/problems/find-all-groups-of-farmland/

from typing import List
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        numRows, numCols = len(land), len(land[0])
        result = []

        for i in range(numRows):
            for j in range(numCols):
                if land[i][j] == 1:
                    topLeft = [i, j]
                    bottomRight = [i, j]
                    stack = [(i, j)]
                    land[i][j] = -1
                    
                    while stack:
                        row, col = stack.pop()
                        for dRow, dCol in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            newRow, newCol = row + dRow, col + dCol
                            if 0 <= newRow < numRows and 0 <= newCol < numCols and land[newRow][newCol] == 1:
                                stack.append((newRow, newCol))
                                topLeft[0] = min(topLeft[0], newRow)
                                topLeft[1] = min(topLeft[1], newCol)
                                bottomRight[0] = max(bottomRight[0], newRow)
                                bottomRight[1] = max(bottomRight[1], newCol)
                                land[newRow][newCol] = -1
                    
                    result.append(topLeft + bottomRight)
        
        return result
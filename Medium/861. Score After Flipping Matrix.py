# 861. Score After Flipping Matrix
# https://leetcode.com/problems/score-after-flipping-matrix/

from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Step 1: Toggle rows to ensure the MSB is 1
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        
        # Step 2: Calculate the score without toggling columns
        score = (1 << (n - 1)) * m  # MSB of each row contributes 2^(n-1) to the score
        for j in range(1, n):
            count1s = sum(grid[i][j] for i in range(m))
            score += max(count1s, m - count1s) * (1 << (n - 1 - j))  # Add contribution of each column
        
        return score
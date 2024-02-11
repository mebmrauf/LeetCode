# 1463. Cherry Pickup II
# https://leetcode.com/problems/cherry-pickup-ii/description/
# https://leetcode.com/problems/cherry-pickup-ii/solutions/4712104/dp-solution-cherry-collection-by-two-robots-in-a-grid/

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Initialize a 3D DP array
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]
        
        def getCherries(row, col1, col2):
            # Check if the robots are out of bounds or at a forbidden cell
            if row == rows or col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return 0
            
            # If the result for this state is already calculated, return it
            if dp[row][col1][col2] != -1:
                return dp[row][col1][col2]
            
            # Calculate the cherries collected by both robots at the current cell
            cherries = grid[row][col1] + (col1 != col2) * grid[row][col2]
            
            # Calculate the maximum cherries collected by both robots from the next row
            nMax = 0
            for nCol1 in range(col1 - 1, col1 + 2):
                for nCol2 in range(col2 - 1, col2 + 2):
                    nMax = max(nMax, getCherries(row + 1, nCol1, nCol2))
            
            # Update the DP array with the result
            dp[row][col1][col2] = cherries + nMax
            return dp[row][col1][col2]
        
        return getCherries(0, 0, cols - 1)
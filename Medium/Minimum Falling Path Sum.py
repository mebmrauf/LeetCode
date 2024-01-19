# 931. Minimum Falling Path Sum
# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix)
        
        for row in range(1, n):
            for col in range(n):
                matrix[row][col] += min(matrix[row-1][max(col-1, 0)], matrix[row-1][col], matrix[row-1][min(col+1, n-1)])

        return min(matrix[-1])
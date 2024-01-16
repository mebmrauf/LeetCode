# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row0, col0 = set(), set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row0.add(i)
                    col0.add(j)

        for row in row0:
            for j in range(cols):
                matrix[row][j] = 0

        for col in col0:
            for i in range(rows):
                matrix[i][col] = 0


                
        """
        Do not return anything, modify matrix in-place instead.
        """
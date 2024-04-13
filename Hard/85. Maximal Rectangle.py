# 85. Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        def largestRectangleArea(heights: List[int]) -> int:
            stack, maxArea = [], 0
            heights.append(0)
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, h * w)
                stack.append(i)
            return maxArea
        
        m, n = len(matrix), len(matrix[0])
        heights, maxArea = [0] * n, 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxArea = max(maxArea, largestRectangleArea(heights))
        
        return maxArea
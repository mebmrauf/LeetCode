# 79. Word Search
# https://leetcode.com/problems/word-search/

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def backtrack(row, col, index):
            if index == len(word):
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
                return False
            
            temp, board[row][col] = board[row][col], '#'
            
            if (backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col, index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1)):
                return True
            
            board[row][col] = temp
            return False
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        
        return False
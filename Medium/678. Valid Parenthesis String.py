# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        lower = upper = 0
        for char in s:
            if char == '(':
                lower += 1
                upper += 1
            elif char == ')':
                lower -= 1
                upper -= 1
            else:
                lower -= 1
                upper += 1
            if upper < 0:
                return False
            lower = max(lower, 0)
        return lower == 0
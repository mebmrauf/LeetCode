# 3174. Clear Digits
# https://leetcode.com/problems/clear-digits/

from collections import deque

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = deque()

        for i in s:
            if not i.isdigit():
                stack.append(i)
            elif stack:
                stack.pop()
        
        return "".join(stack)
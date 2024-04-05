# 1544. Make The String Great
# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) == 0 or abs(ord(stack[-1]) - ord(char)) != 32:
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)        